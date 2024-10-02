# Stage 2: Get PDFs

We use the 'playwright' python package to download the pdfs of research papers, using the open-access URLs we found and saved in Stage 1.

## Package Installation

Assuming a conda environment called vis-sieve has already been created, install playwright package with:

```
conda activate vis-sieve
conda config --add channels conda-forge
conda config --add channels microsoft
conda install playwright
playwright install # needed to download new browsers
```

## Steps

1. **Download pdfs**  
Run 02_get-pdfs/get-pdfs.py script.

    ```
    # example for CSR's code
    # ****************************
    # script assumes root folder is 'current/' 
    cd current
    python 02_get-pdfs/get-pdfs.py \
    16 50 \
    --database database/publications_princeton.db \
    --cyverse_prefixpath /iplant/home/carolinarr/vis-sieve/Princeton_content/ 
    ```

2. **Update databases**   
    a. Update **Cyverse** database:   
    Need to upload the pdf files to Cyverse database using Go commands.
    ```
    # 1. Open 'database/cyv_upload-pdfs.sh' file
    vim database/cyv_upload-pdfs.sh
    # 2. Update variables as needed in lines 36-37
    # 3. Execute file
    database/cyv_upload-pdfs.sh
    ```  
    b. Update **DuckDB** database:
    Need to update the 'pdf_path' column in the DuckDB 'papers' table with URLs to pdfs on Cyverse.
    Run 'database/db_modify_database_pdfpath.py' file.
    ```
    # example for CSR's code
    # ****************************
    # script assumes root folder is 'current/' 
    cd current
    python database/db_modify_database_pdfpath.py \
    --database database/publications_princeton.db \
    --cyverse_pdfpaths database/data/cyverse_pdfs_paths_2024-08-15_09-52-25.csv
    ```

3. **Clean up files**  
Once pdfs are on Cyverse, can clean up your local files by deleting pdf files and list of paths to the pdfs.
    ```
    cd database
    # delete local pdfs
    rm -r content/     
    # delete associated                   
    rm database/data/cyverse_pdf_paths*  files
    ```