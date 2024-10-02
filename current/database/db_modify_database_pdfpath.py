# Update DuckDB 'papers' table with paths to pdfs files in Cyverse  
# ****************************************************************
# (performed as part of process in step02_get-pdfs.)

# updates column "pdf_path" in 'papers' table
# assumes you are running from 'current' folder

# modules that need to be installed
import duckdb as db
import pandas as pd

# modules that come with python (no need to install)
# See: https://docs.python.org/3/py-modindex.html#cap-d
import argparse
import asyncio
import os
from pathlib import Path

async def main():
    parser = argparse.ArgumentParser(description = "Fill in 'pdf_paths' to DuckDB 'papers' table")
    parser.add_argument("--database", help = "path of duckdb database file, e.g., 'publications_princeton.db'")
    parser.add_argument("--cyverse_pdfpaths", help = "path of .csv file containing list of cyverse urls for pdfs, e.g., 'database/data/cyverse_pdfs_paths_2024-08-15_09-52-25.csv'")
    args = parser.parse_args()

    # Import data 
    # (list of links to pdfs on Cyverse database)
    links_location = args.cyverse_pdfpaths # class 'str'
    links = pd.read_csv(links_location, header=None, names=["cyverse_pdf_path", "paper_id"])

    # Connect to DuckDB database
    db_duckdb_path = Path(args.database) # class 'pathlib.PosixPath'
    con = db.connect(str(db_duckdb_path))

    # Add links-to-pdfs-on-Cyverse to 'pdf_path' column in DuckDB's 'paper' table
    ## Steps:
    # a. Register links pandas dataframe as a table
    con.register('temp_pdf_paths_df', links)
    ## b1. create temporary (temp) table
    ## b2. update 'paper' table with links from temp table
    ## b3. delete temp table
    con.execute(f"""

            CREATE TABLE temp_pdf_paths AS
                SELECT * FROM temp_pdf_paths_df;
                
            UPDATE paper
                SET pdf_path = cyverse_pdf_path
                FROM temp_pdf_paths
                WHERE temp_pdf_paths.paper_id = paper.id;

            DROP TABLE temp_pdf_paths;
                
            """)

    # *** Code for Testing ***
    # links = pd.read_csv('database/data/cyverse_pdfs_paths_2024-08-15_09-52-25.csv', header=None, names=["cyverse_pdf_path", "paper_id"])

    # # just testing that connection is working
    # result = con.execute("SELECT * FROM paper").fetchall()
    # print(result)
    
    # print(db_duckdb_path)
    # print(type(db_duckdb_path))
    # print(links_path)
    # print(type(links_path))
    # print(links.head())
    # print(type(links))

    con.close()

if __name__ == '__main__':
    asyncio.run(main())