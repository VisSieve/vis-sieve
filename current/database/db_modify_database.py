# Make changes to existing database, need for 05_visualization step

import duckdb as db
import tqdm
import os
from pathlib import Path
import requests as rq
import json

os.system('pwd') 
con = db.connect("publications_princeton.db")

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

# Update data in Atlas table
#******************************************
# updates one row
con.execute(f"""
            UPDATE atlas
            SET server_path = '{row1[1]}' WHERE id = 1;
            """)

con.close()

#************************************************************************************
#       ADDING TO FIGURE_PROPERTY TABLE
#************************************************************************************

# Add columns xPos, yPos, zPos
con.execute("ALTER TABLE figure_property ADD COLUMN xPos INTEGER;")
con.execute("ALTER TABLE figure_property ADD COLUMN yPos INTEGER;")
con.execute("ALTER TABLE figure_property ADD COLUMN zPos INTEGER;")

con.close()