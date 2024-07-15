# Script to Explore Database files
# Created by Carolina Roe-Raymond (c.roe-raymond@princeton.edu); July 
# 2024.
import duckdb as db
import os
from tabulate import tabulate # pretty print tabular information

# Connect to Data
# ------------------------------------------

# Choose data file (run only one of these lines)
current_file = 'current/publications_princeton_2023.db'
current_file = 'publications_princeton.db'

# # (for troubleshooting) check working directory, to check path to 'current_file' 
# os.system('pwd') 

# connect to database
con = db.connect(f"{current_file}")

# List Database's Tables
# ------------------------------------------
con.sql("SHOW ALL TABLES;")

# Save above information
db_tables = con.execute("SHOW ALL TABLES;").fetchall()

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
con.sql("""
    SELECT *
    FROM figure_property
    LIMIT 10;
    """)

# Calculate Total Number of Rows in a Table
# ------------------------------------------
# Execute the query to get the total number of rows
table_name = 'atlas'
total_rows = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
print(total_rows)