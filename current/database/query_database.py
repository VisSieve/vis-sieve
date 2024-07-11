# Script to Explore Database files

import duckdb as db
import os

os.system('pwd')
con = db.connect('publications_princeton.db')

# View All Tables
# ------------------------------------------
con.sql("""
            SHOW ALL TABLES;
            """)
print(con.fetchall())

# Describe Each Table
# ------------------------------------------
