# Make changes to existing database, need for 05_visualization step

import duckdb as db
import os

os.system('pwd') 
con = db.connect("database/publications_princeton.db")

#************************************************************************************
#       UPDATE A ROW IN A TABLE
#************************************************************************************

#updates one row of <insert-table> database
table = atlas
column = server_path
data_to_insert = row1[1]
id = 1
con.execute(f"""
            UPDATE {table}
            SET {column} = '{data_to_insert}' WHERE id = {id};
            """)

#************************************************************************************
#       ADDING ATLAS TABLE
#************************************************************************************

# Add an Atlas table
#******************************************
con.execute('DROP TABLE IF EXISTS atlas;')
con.execute('''
            CREATE TABLE atlas (
                id BIGINT,
                server_path VARCHAR,
                width BIGINT,
                height BIGINT
            );
            ''')

# Add data to Atlas table
#******************************************

# data to be added
row1 = [1, "https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_atlas/atlas-1.jpg", 64, 64] 
row2 = [2, "https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_atlas/atlas-2.jpg", 64, 64]
row3 = [3, "https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_atlas/atlas-3.jpg", 64, 64]
# !!! this link wasn't working
row4 = [4, "https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_atlas/atlas-4.jpg", 64, 35] 

# # add to database (for the first time)
# con.execute(f"""
#             INSERT INTO atlas 
#             VALUES 
#             ({row1[0]}, '{row1[1]}', {row1[2]}, {row1[3]}),
#             ({row2[0]}, '{row2[1]}', {row2[2]}, {row2[3]}),
#             ({row3[0]}, '{row3[1]}', {row3[2]}, {row3[3]}),
#             ({row4[0]}, '{row4[1]}', {row4[2]}, {row4[3]});
#             """)

# Update one row in a table
#******************************************

table = 'figure_property'
colname = 'xPos'
value_to_add = row1[1]

con.execute(f"""
            UPDATE {table}
            SET {colname} = '{value_to_add}' WHERE id = 1;
            """)

con.close()

#************************************************************************************
#       ADD A NEW COLUMN TO A TABLE
#************************************************************************************

table = 'paper'
colname = 'pdf_retrieved'
coltype = 'VARCHAR(10)'

con.execute(f"""
            ALTER TABLE {table} ADD COLUMN {colname} {coltype};
            """)
con.close()
