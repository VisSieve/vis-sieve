# Script to Explore Database files
# Created by Carolina Roe-Raymond (c.roe-raymond@princeton.edu); July 
# 2024.
import duckdb as db
import pandas as pd
import os
from tabulate import tabulate # pretty print tabular information


# Connect to Data
# ------------------------------------------

# (for troubleshooting) check working directory, to check path to 'current_file' 
os.system('pwd') 

# Choose data file (run only one of these lines)
current_file = 'database/publications_princeton_2023.db'
current_file = 'test2.db'

# connect to database
con = db.connect(f"{current_file}")

# List Database's Tables
# ------------------------------------------
con.sql("SHOW ALL TABLES")

# Save above information
# to python
db_tables = con.execute("SHOW ALL TABLES;").fetchall()
# to csv
result = con.execute("SHOW ALL TABLES").fetchdf()
result.to_csv('database/db_structure.csv', index=False)


# Save above headers
# # con.description contains the column names of database table
# # to get the column names, extract the first item of each tuple in con.description
db_tables_headers = [item[0] for item in con.description]

# Print Table Structures
# ------------------------------------------
# column names for tables
table_headers = ['column_name', 'column_type', 'null', 'key', 'default', 'extra']

for item in db_tables:
    # grab table name
    table = [item[2]]
    # convert to string
    table_str = str(table[0])
    # get table contents
    table_description = con.execute(f"DESCRIBE {table_str};").fetchall()
    # display findings
    print(table_str, 'TABLE')
    print('********************************************')
    print(tabulate(table_description, headers = table_headers))
    print('\n')


# View Data Within Specific Table
# ------------------------------------------

table_name = 'paper'
col_name = 'id'

# View entire table
con.sql(f"""
    SELECT *
    FROM {table_name}
    """)

# View head of table (first few rows)
con.sql(f"""
    SELECT *
    FROM {table_name}
    OFFSET 150 ROWS
    LIMIT 200;
    """)

# View total number of rows
total_rows = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
print(total_rows)

# Select rows that contain VALUE for a certain column
con.sql(f"""
    SELECT *
    FROM {table_name}
    WHERE {col_name} = 4367319112
    """)

# View range of a date column
query = f"""
        SELECT MIN({col_name}) AS min_date, 
        MAX({col_name}) AS max_date
        FROM {table_name};
        """
# Execute the query and fetch the result
result = con.execute(query).fetchall()
# Extract the minimum and maximum dates
min_date, max_date = result[0]
print(f"Date range: {min_date} to {max_date}")

# Select rows that contain NULL for a certain column
con.sql(f"""
    SELECT *
    FROM {table_name}
    WHERE {col_name} IS NULL
    """)


con.close()