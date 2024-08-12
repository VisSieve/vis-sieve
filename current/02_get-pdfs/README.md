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

## Running the Script

with Carolina's code
```
# must run from Carolina's 'current' folder
cd current
python 02_get-pdfs/get-pdfs.py \
16 50 \
--database database/publications_princeton.db \
--cyverse_prefixpath /iplant/home/carolinarr/vis-sieve/Princeton_content/ 
```