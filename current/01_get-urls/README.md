# Stage 1: Get URLs

## Diagram of Function in get-urls.py

![Alt](../../images/function-diagram_get-urls.py.png) "Boxes listing each function in the get-urls.py script and links between which function calls which other function.")


## Package Installation

To install packages:

```
conda create --name vis-sieve requests tqdm
conda activate vis-sieve
pip install duckdb --upgrade
```

## Database Creation

In database/ folder, within README.md see 'Database Creation Instructions' under 'DuckDB Information' section for code on creating database.

## Running the Script

To run the command for the year 2023, for example...

with Devin's code:
```
# if running from Devin's code
python 01_02_hear_me_ROR_script_dates.py 2023 2023 --ror 00hx57361 --output hear_me_ror_test_2022-01.json -a --database publications_TEST_dates.db --content_root test_dates/
```

with Carolina's code
```
# must run from Carolina's 'current' folder
cd current
python -m 01_get-urls.get-urls \
2019 2019 \
--ror 00hx57361 \
--email c.roe-raymond@princeton.edu \
--output urls.json \
-a \
--database database/publications_princeton.db \
--content_root results/ 
```

Because of the way Carolina's folders are organized, need to run the command from the 'current' folder, but then run the desired python script (01_get-urls/get-urls.py) as a module by using the -m tag and calling the script as a module  with the '.' in the path. This approach ensures we don't need to modify sys.path.

Also note that in Carolina's script we attempted to make the email a command line argument (not yet implemented in Devin's code as of July 2024).