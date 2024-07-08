# 'Current' Code for Carolina

This folder contains scripts, data, code, that Carolina is currently digging into.

## Description of Files

* **hear_me_ROR_script_copied-YYYY-MM-DD.py** - code that:
    + [url-grab] grabs links from all papers produced at an institution for a set of years (from OpenAlex)
    + [pdf-grab] download the pdfs from those links (Python's playwright library)
    + [database-add] adds information on the institution, authors, papers, etc. to a DuckDB file (Python's duckdb library)
* **get-figs.md** - describes the process to install tool that grabs figures from all downloaded pdfs
