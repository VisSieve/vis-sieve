# get-pdfs-multiprocessing.py
# developed by Carolina Roe-Raymond with ChatGPT4o on 2024-11-01

import subprocess as sp
import logging
import argparse
import multiprocessing as mp
import os
from pathlib import Path
import duckdb

# Set up argument parsing to retrieve command-line arguments
parser = argparse.ArgumentParser(description="Multiprocess PDF download.")
parser.add_argument("num_pdfs", type=int, help="Total number of PDFs to download.")
parser.add_argument("db_file", type=str, help="DuckDB database file to source URLs.")
parser.add_argument("num_cores", type=int, help="Number of cores to use for multiprocessing.")
args = parser.parse_args()

# Set up logging for tracking process statuses
logging.basicConfig(filename='download_log.log', level=logging.INFO)
logger = logging.getLogger(__name__)

# Extract the year from the DuckDB file name to organize PDFs in folders
db_year = args.db_file.split('_')[-1][:4]

# Create a folder for PDFs if it doesn't already exist
pdf_dir = Path("pdfs") / db_year
pdf_dir.mkdir(parents=True, exist_ok=True)

# Connect to the DuckDB database to fetch URLs for downloading
con = duckdb.connect(args.db_file)
query = f"""
    SELECT id, oa_url
    FROM papers
    WHERE pdf_retrieved IS NULL
    ORDER BY publication_date, pdf_retrieved
    LIMIT {args.num_pdfs};
"""
urls_to_download = con.execute(query).fetchall()  # Retrieve records for processing

# Calculate how many PDFs each core will process
pdfs_per_core = args.num_pdfs // args.num_cores
if args.num_pdfs % args.num_cores != 0:
    pdfs_per_core += 1  # Add one more to distribute remainder

# Split URLs into chunks for each core
url_chunks = [urls_to_download[i:i + pdfs_per_core] for i in range(0, len(urls_to_download), pdfs_per_core)]

def download_pdf_process(records):
    """Executes the PDF download for a chunk of records by calling get-pdfs.py.
    
    Args:
        records (list): List of tuples, each containing (id, url) for a paper to be downloaded.
        
    Returns:
        list: List of tuples with Paper ID and boolean indicating success for each record.
    """
    results = []
    for paper_id, url in records:
        pdf_path = pdf_dir / f"{str(paper_id)}.pdf"
        
        # Call get-pdfs.py with subprocess to handle the download
        try:
            result = sp.run(["python", "get-pdfs.py", "--url", url, "--destination", str(pdf_path)], capture_output=True)
            success = result.returncode == 0  # True if download succeeded
        except Exception as e:
            logger.error(f"Failed to download for ID {paper_id}: {e}")
            success = False
        
        # Log the result in download_log.log
        logger.info(f"ID: {paper_id}, Success: {success}")
        results.append((paper_id, success))  # Store result for each PDF
    return results

# Set up multiprocessing with the specified number of cores
with mp.Pool(args.num_cores) as pool:
    results = pool.map(download_pdf_process, url_chunks)

# Flatten results and update database with download status once all processes are complete
flat_results = [item for sublist in results for item in sublist]
update_query = """
    UPDATE papers 
    SET pdf_retrieved = CASE id 
        {cases}
        ELSE pdf_retrieved END
    WHERE id IN ({ids});
"""
case_statements = ", ".join(
    f"WHEN {paper_id} THEN {'TRUE' if success else 'FALSE'}" for paper_id, success in flat_results
)
id_list = ", ".join(str(paper_id) for paper_id, _ in flat_results)

con.execute(update_query.format(cases=case_statements, ids=id_list))
con.close()