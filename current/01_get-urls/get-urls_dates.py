"""
file: hear_me_ROR_script.py
author: Ben Kruse
Adapted from: hear_me_ROR.ipynb by Devin Bayly
Adapted by: ChatGPT 4o with Carolina Roe-Raymond, to use dates (YYYY-MM-DD) instead of years as input

Takes a ROR identification of school and a range of years,
then generates a json file with the publications of the school
for that period
"""

# modules that need to be installed
import requests as rq
from tqdm import tqdm
import duckdb as db 

# modules that come with python (no need to install)
# See: https://docs.python.org/3/py-modindex.html#cap-d
import argparse
from datetime import datetime, timedelta
import json
import math
import os
from pathlib import Path

# modules we've written
from database.db_create_database import create

def remove_duplicate_authors(publications, silent=False):
    """Removes duplicate authors from a list of publications"""
    for pub in publications:
        authors = pub["authorships"]
        seen_ids = set()
        new_authors = []
        for a in authors:
            if a["author"]["id"] not in seen_ids:
                new_authors.append(a)
                seen_ids.add(a["author"]["id"])
            else:
                if not silent:
                    print(f"Duplicate author in {pub['title']}: {a['author']['display_name']}")
        pub["authorships"] = new_authors
    return publications

def generate_date_range(start_date, end_date):
    """Generate a range of dates from start_date to end_date inclusive"""
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    return date_list

def safe_json_load(response):
    """Safely load JSON data from a response"""
    try:
        return response.json()
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from response: {response.text}")
        return None

def results_per_date(date, ror="03m2x1q45", silent=False, filter_duplicate_authors=True, testing=False):
    """Gets the publications for a school for a specific date"""
    all_res = []
    headers = {"mailto":"baylyd@arizona.edu"} ## Make command line arg
    url = f"https://api.openalex.org/works?filter=from_publication_date:{date},to_publication_date:{date},institutions.ror:{ror}&cursor=*&per-page=200"
    res = rq.get(url, headers=headers)
    data = safe_json_load(res)
    if not data:
        return all_res

    if filter_duplicate_authors:
        data["results"] = remove_duplicate_authors(data["results"], silent=silent)
    page_count = data["meta"]["count"] / data["meta"]["per_page"]
    all_res.extend(data["results"])
    cursor = data["meta"]["next_cursor"]
    query = 0
    if not silent:
        pbar = tqdm(total=math.ceil(page_count))
    while cursor:
        query += 1
        res = rq.get(f"{url}&cursor={cursor}")
        
        data = safe_json_load(res)
        if not data:
            break

        if filter_duplicate_authors:
            data["results"] = remove_duplicate_authors(data["results"], silent=silent)
        all_res.extend(data["results"])
        cursor = data["meta"].get("next_cursor", None)
        if not silent:
            pbar.update(1)
        if testing:
            break
    return all_res

def get_publications(ror: str, dates: list, output_file: str, silent=False, get_authors=False):
    """Gets the publications for a school for a range of dates and writes them to a json file"""
    all_res = []
    for date in dates:
        if not silent:
            print(f"Getting publications for {date}")
        all_res.extend(results_per_date(date, ror, silent))
    with open(output_file, "w") as f:
        json.dump(all_res, f)

    if get_authors:
        if not silent:
            print("Getting authors")
        with open("authors" + output_file, "w") as f:
            json.dump(get_all_authors(all_res, output_file), f)

def get_all_authors(publications, output_file):
    """Gets the authors from a list of publications"""
    authors = {}
    author_ids = {}
    for pub in publications:
        for a in pub["authorships"]:
            publication = {
                "work_id": pub["id"],
                "author": {
                    "id": a["author"]["id"],
                    "display_name": a["author"]["display_name"],
                    "orcid": a["author"]["orcid"]
                },
                "open_access": pub["open_access"]
            }
            if a["author"]["id"] not in author_ids:
                pub_array = [publication]
                author_ids[a["author"]["id"]] = pub_array
                authors[a["author"]["display_name"]] = pub_array
            else:
                author_ids[a["author"]["id"]].append(publication)
    return authors

def add_institution_to_db(con: db.DuckDBPyConnection, institution_ror: str = None, institution_name: str = None, institution_id: int = None) -> int:
    """Adds an institution to the database"""
    if institution_ror is not None:
        institution_info = rq.get(f"https://api.openalex.org/institutions/https://ror.org/{institution_ror}").json()
        institution_name = institution_name or institution_info["display_name"]
        institution_id = institution_id or int(institution_info["id"].split("I")[-1])

    elif institution_id is not None:
        con.execute(f"SELECT COUNT(1) FROM institution WHERE id = {institution_id};")
        exists = con.fetchone()[0]
        if exists:
            return institution_id
        
        institution_info = rq.get(f"https://api.openalex.org/institutions/I{institution_id}").json()
        institution_name = institution_name or institution_info["display_name"]
        institution_ror = institution_ror or institution_info["ror"].split("/")[-1]
        
    institution_name = institution_name.replace("'", "")
    try:
        con.execute(f"INSERT INTO institution VALUES ({institution_id}, '{institution_ror}', '{institution_name}');")
    except db.ConstraintException:
        pass

    return institution_id

def populate_database(database_file: str, ror: str, dates: list, content_root: str, json_output: str = None, silent: bool = False) -> None:
    """Populates a database with publications for a school for a range of dates"""
    con = db.connect(database_file)
    inst_id = add_institution_to_db(con, institution_ror=ror)

    for date in dates:
        if not silent:
            print(f"Getting publications for {date}, database version")
        publications = results_per_date(date, ror, silent, testing=True)
        print("Processing publications")
        for pub in tqdm(publications):

            pub_date = pub["publication_date"]
            pub_id = int(pub["id"].split("W")[-1])
            pub_title = pub["title"][:200].replace("'", "")
            pub_doi = pub["doi"]
            pub_oa_url = pub["open_access"]["oa_url"]
            pub_inst_id = inst_id
            pub_oa_status = pub["open_access"]["oa_status"]

            con.execute(f"SELECT COUNT(1) FROM paper WHERE id = {pub_id};")
            exists = con.fetchone()[0]
            
            if exists:
                continue

            con.execute(f"""INSERT INTO paper (id, title, doi, publication_date, oa_url, inst_id) VALUES ({pub_id}, '{pub_title}', '{pub_doi}', '{pub_date}', '{pub_oa_url}', '{pub_inst_id}');""")
            for a in pub["authorships"]:
                institutions = a["institutions"]
                rors = [Path(i["ror"]).stem for i in institutions]
                if ror in rors:
                    try:
                        con.execute(f"""INSERT INTO author VALUES ({a['author']['id'].split('A')[-1]}, '{a['author']['display_name'].replace("'", "")}');""")
                    except db.ConstraintException:
                        pass

                    try:
                        con.execute(f"INSERT INTO contribution VALUES ({a['author']['id'].split('A')[-1]}, {pub['id'].split('W')[-1]});")
                    except db.ConstraintException:
                        pass
                    
                    for author_inst in a["institutions"]:
                        add_institution_to_db(con, institution_id=int(author_inst["id"].split("I")[-1]))
                        try:
                            con.execute(f"INSERT INTO residence VALUES ({a['author']['id'].split('A')[-1]}, {author_inst['id'].split('I')[-1]});")
                        except db.ConstraintException:
                            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get publications for a school")
    parser.add_argument("first_date", help="First date to get publications for (YYYY-MM-DD)")
    parser.add_argument("last_date", help="Last date to get publications for (YYYY-MM-DD)")
    parser.add_argument("--ror", help="ROR of the school (UofA by default)", default="03m2x1q45")
    parser.add_argument("--output", help="Output file name", default="hear_me_ROR_out.json")
    parser.add_argument("-a", "--get_authors", help="Get authors as well as publications", action="store_true")
    parser.add_argument("-s", "--silent", help="Silence output", action="store_true")
    parser.add_argument("--database", help="Database file to store publications in")
    parser.add_argument("--content_root", help="Root directory for content")
    args = parser.parse_args()

    first_date = datetime.strptime(args.first_date, "%Y-%m-%d")
    last_date = datetime.strptime(args.last_date, "%Y-%m-%d")
    date_range = generate_date_range(first_date, last_date)
    
    if args.database:
        db_file = Path(args.database)
        if not db_file.exists():
            print("creating", db_file)
            create(db_file)
        populate_database(args.database, args.ror, date_range, args.content_root, args.output, args.silent)
    else:
        get_publications(args.ror, date_range, args.output, args.silent, args.get_authors)