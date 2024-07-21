import duckdb as db

def create(name):
    # TODO add in code to handle if the .db isn't added
    con = db.connect(f'{name}')
    con.execute('''
                DROP TABLE IF EXISTS atlas;
                DROP TABLE IF EXISTS author;
                DROP TABLE IF EXISTS charts;
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
            FROM read_csv('data/atlas.csv',
                header = TRUE
            ); 
                    
        CREATE TABLE author (
            id BIGINT,
            name VARCHAR(100) NOT NULL
        );    

        CREATE TABLE charts AS
            SELECT * 
            FROM read_csv('data/charts.csv',
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
        );
                    
        CREATE TABLE figure_property (
            name VARCHAR(100),
            int_value INTEGER,
            string_value VARCHAR(100),
            figure_id BIGINT,
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
            pdf_path VARCHAR(150),
            inst_id BIGINT,
        );                

        CREATE TABLE residence (
            au_id BIGINT,
            inst_id BIGINT,
        );
        
        CREATE TABLE topic AS
            SELECT * 
            FROM read_csv('data/openalex_topic-mapping-table_utf8_downloaded2024-07-17.csv',
                header = TRUE
            # creates columns:
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
            );        
        
        CREATE TABLE paper_topic (
            paper_id BIGINT,
            topic_id BIGINT,
            topic_score DOUBLE
        ); 
                
    ''')

    con.close()