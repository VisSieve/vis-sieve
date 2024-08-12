# modules that need to be installed
import duckdb
from playwright.async_api import Playwright, async_playwright, expect

# modules that come with python (no need to install)
# See: https://docs.python.org/3/py-modindex.html#cap-d
import argparse
import asyncio
import os
import sys
from pathlib import Path

async def grab_pdf(oa_url, destination, playwright) -> bool:
    browser = await playwright.chromium.launch_persistent_context(
        '/tmp/playwright',
        accept_downloads=True, 
        headless=True, 
        slow_mo=1000)
    browser.set_default_timeout(10000)
    page = await browser.new_page()

    try:
        async with page.expect_download() as download_info:
            try:
                await page.goto(oa_url, timeout=0)
            except:
                print("Saving file to ", destination)
                # Wait for the download to start
                download = await download_info.value
                # Wait for the download process to complete
                print(await download.path())
                # Save downloaded file somewhere
                await download.save_as(
                    str(destination)
                )
                # await download.save_as(os.path.join(downloads_path, file_name))
            await page.wait_for_timeout(200)
            await browser.close()
            return True
    except Exception as e:
        await browser.close()
        return False
        

# def strip_figures(pdf_path, output_dir):
#     os.system('pdfimages ' + pdf_path + ' ' + output_dir)
#     #os.system('cd ' + output_dir + ' && rm ./*.ppm -f && rm ./*.pbm -f')
#     return

# def get_figures(pdf_dir_path, output_dir):
#     #TODO replace the os.path stuff with Path
#     for subfolder in os.listdir(pdf_dir_path)[:500]:
#         subfolder_path = os.path.join(pdf_dir_path, subfolder)
#         pdf_path = os.path.join(subfolder_path, os.listdir(subfolder_path)[0])
#         print(pdf_path)

#         sub_out_dir = os.path.join(output_dir, subfolder)
#         if not os.path.exists(sub_out_dir):
#             os.makedirs(sub_out_dir)
        
#         strip_figures(pdf_path, sub_out_dir+'/')


async def main():
    # use argparse to get information about the pdfs we are gathering 
    # just a work id, and a publications.db file should be enough
    parser = argparse.ArgumentParser(description = "Get pdfs of papers in database")
    parser.add_argument("row_start", help = "database row to start gathering pdfs for, e.g., 1")
    parser.add_argument("row_end", help = "database row to stop gathering pdfs for, e.g., 100")
    parser.add_argument("--database", help = "path of duckdb database file, e.g., 'publications_princeton.db'")
    parser.add_argument("--cyverse_prefixpath", help = "path of cyverse database location where pdfs will be uploaded, e.g., '/iplant/home/<username>/vis-sieve/'")
    args = parser.parse_args()
    
    # Connect to database
    db_path = Path(args.database)
    con = duckdb.connect(str(db_path))

    # Make the content parent folder
    content_root_path = Path("content")
    content_root_path.mkdir(exist_ok=True)

    # Establish rows of data to use for pdf grab
    offset = int(args.row_start) - 1 
    num_rows = int(args.row_end) - offset
    print("Grabber Initialized. NUM of ROWS: ", num_rows, "; STARTING AFTER ROW: ", offset)
    
    async with async_playwright() as playwright:
        papers = con.sql(f"SELECT * from paper LIMIT {num_rows} OFFSET {offset}").fetchall()
        for paper in papers:
          pub_id = paper[0]
          pub_folder = Path(f"{content_root_path}/{pub_id}")
          pub_folder.mkdir(exist_ok=True)
          pdf_path = Path(f"{pub_folder}/{pub_id}.pdf")
          # grab the url from the correct index
          print("PAPER: ", paper)
          pub_oa_url = paper[4]
          print("PUB_OA_URL: ",pub_oa_url)
          pdf_grab_result = await grab_pdf(pub_oa_url, pdf_path, playwright)
          print("PDF Retrieved? --->", pdf_grab_result)
          
          # adding to 'paper' TABLE, 'pdf_grab_result' column
          # *******************
          # Add whether pdf retrieval result was True or False to database
          con.execute(f"""
            UPDATE paper
            SET pdf_retrieved = '{pdf_grab_result}' WHERE id = {pub_id};
            """)
          
          # now perform the duckdb updates?
          cyverse_path = Path(args.cyverse_prefixpath)
          print(cyverse_path)


if __name__ == '__main__':
    asyncio.run(main())


    # create a playwright instance
    # run the get_pdf system
    #get_figures(sys.argv[1], sys.argv[2])