import duckdb as db
import pandas as pd

def create(name):
    
    con = db.connect(f'{name}')
    
    con.execute('''
                DROP TABLE IF EXISTS atlas;
                DROP TABLE IF EXISTS author;
                DROP TABLE IF EXISTS charttypes;
                DROP TABLE IF EXISTS contribution;
                DROP TABLE IF EXISTS figure;
                DROP TABLE IF EXISTS figure_property;
                DROP TABLE IF EXISTS institution;
                DROP TABLE IF EXISTS paper;
                DROP TABLE IF EXISTS residence;
                DROP TABLE IF EXISTS topic;
                DROP TABLE IF EXISTS paper_topic;
                ''')

    con.execute('''
    
        CREATE TABLE atlas AS
            SELECT * 
            FROM read_csv('database/data/atlas.csv',
                header = TRUE
            ); 
                    
        CREATE TABLE author (
            id BIGINT,
            name VARCHAR(100) NOT NULL
        );    

        CREATE TABLE charttypes AS
            SELECT * 
            FROM read_csv('database/data/charttypes.csv',
                header = TRUE
        );   
                
        CREATE TABLE contribution (
            au_id BIGINT,
            paper_id BIGINT,
        );
                    
        CREATE TABLE figure (
            id BIGINT ,
            paper_id BIGINT,
            local_path VARCHAR(150),
            server_path VARCHAR(150),
            caption VARCHAR(1000)
        );
                    
        CREATE TABLE figure_property (
            id BIGINT,
            figure_id BIGINT,
            charttype_id BIGINT,
            xPos INTEGER,
            yPos INTEGER,
            zPos INTEGER,
            score DOUBLE
        );
                    
        CREATE TABLE institution (
            id BIGINT ,
            ror VARCHAR(20) NOT NULL,
            name VARCHAR(100) NOT NULL
        );
    
        
        CREATE TABLE paper (
            id BIGINT ,
            title VARCHAR(200) NOT NULL,
            doi VARCHAR(100),
            publication_date DATE,
            oa_url VARCHAR(200),
            oa_status VARCHAR(20),
            pdf_retrieved VARCHAR(10),
            pdf_path VARCHAR(150),
            inst_id BIGINT,
        );                

        CREATE TABLE residence (
            au_id BIGINT,
            inst_id BIGINT,
        );
        
        CREATE TABLE topic AS
            SELECT * 
            FROM read_csv('database/data/openalex_topic-mapping-table_utf8_downloaded2024-07-17.csv',
                header = TRUE           
            );        
        
        CREATE TABLE paper_topic (
            paper_id BIGINT,
            topic_id BIGINT,
            topic_score DOUBLE
        ); 
                
    ''')

    # Update db_STRUCTURE.csv file with above structure
    # uses pandas
    result = con.execute("SHOW ALL TABLES").fetchdf()
    result.to_csv('database/db_STRUCTURE.csv', index=False)

    # 'topic' table created with the following columns:
            #  *COLUMN_NAME*  *COLUMN_TYPE*  *NULL*
            #   topic_id       BIGINT         YES
            #   topic_name     VARCHAR        YES
            #   subfield_id    BIGINT         YES
            #   subfield_name  VARCHAR        YES
            #   field_id       BIGINT         YES
            #   field_name     VARCHAR        YES
            #   domain_id      BIGINT         YES
            #   domain_name    VARCHAR        YES
            #   keywords       VARCHAR        YES
            #   summary        VARCHAR        YES
            #   wikipedia_url  VARCHAR        YES  

    con.close()

    print("Success! db file created.")
