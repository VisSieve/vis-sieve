# 'Current' Code for Carolina

This folder contains scripts, data, code, that Carolina is currently digging into/understanding/modifying.

## Project Stages

1. get urls
2. get pdfs
3. get figs
4. label figs
5. visualization

## Description of Project Stages

* [1. get-urls] grabs links from all papers produced at an institution for a set of years (from OpenAlex)
* [2. get-pdfs] download the pdfs from those links, using Python's playwright library
* [3. get figs]
* [4. label figs]
* [5. visualization]
* [database] adds information on the institution, authors, papers, etc. to a DuckDB file (Python's duckdb library)

## Creating a conda environment with all of the needed packages

```
# packages needed for 01_get-urls
conda create --name vis-sieve requests tqdm
conda activate vis-sieve
pip install duckdb --upgrade
```


