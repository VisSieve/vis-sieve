# Database Files

We make use of two databases:
1. **DuckDB Database** - for data (as tables)  
Tables that hold all of the information about our data (e.g. institution id's, paper id's, author id's, figure id's, figure properties, etc.)
2. **Cyverse Database** - for files 
Located within cyverse.org, this remote database holds all of our actual files (pdfs of papers, figure image files, etc.)

## DuckDB Information

Database files that contain information about the institutions, papers, etc. should be created and sourced from within the database/ folder.

### Database Creation Instructions

```
cd current
conda activate vis-sieve
python -i database/db_create_database.py
>>> create('database/<name-of-.db-file>') # example: create(publications_2020.db)
# if needed, use db_query_database.py file to verify db was created as expected
>>> exit()
```
Note: Any .csv's you want to import must use UTF-8 character encoding.

### DuckDB Helpful Links

* [mkdocs DuckDB database](https://vissieve.github.io/main/documentation/site/database/database_information/) documentation (Ben's)
* [data structure](https://github.com/VisSieve/main/blob/Zhiyang-Doc/Visualization/demo-project/src/dbStructure.md), as a list (Zhiyang's)

### DuckDB Explanation of Files
**db_create_database.py**  
creates a duckdb database file (.db file), to be used by hear_me_ROR_script.py (or Carolina's equivalent, get-urls.py script)

**db_modify_atlas_table.py**  
adds information to the atlas table

**db_modify_database.py**  
altered current .db file to make more suitable for visualization work  
(!!! TODO eventually add this to create_database.py file)

**db_query_database.py**  
look at contents of .db files, check for information

## Cyverse Information

### Cyverse Helpful Links

* [Carolina's cyverse content 1](https://de.cyverse.org/data/ds/iplant/home/carolinarr/vis-sieve?type=folder&resourceId=a65f47ce-2da7-11ef-acde-90e2ba675364) (de.cyverse)
* [Carolina's cyverse content 2](https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve) (data.cyverse)
* [Devin's cyverse content](https://data.cyverse.org/dav-anon/iplant/home/baylyd/vis_sieve/) (data.cyverse)

/iplant/home/carolinarr/vis-sieve/Princeton_atlas

### Cyverse Explanation of Files

**cyv_upload.sh**  
example Go commands to upload files to cyverse  
(specifically for user carolinarr, but can be modified)

### Cyverse Data Transfer Instructions

#### Background 
Uses iRODS for data transfer.  

All iRODS commands start with the letter i. For example:
* iget : download
* iput : upload
* iput -P : upload with progress information 

Go commands are essentially iRODS commands.  

In cyverse, dav-anon folder is really about providing an option to share things without users needing to authenticate. To create a shareable link, go to 'Public link' and copy that path. You'll see 'dav-anon' in that path, indicating the 'user' named 'cyverse-anonymous' is allowed to access it.

#### Steps
1. Install Go commands onto computer using instructions here:  
[Transferring Data with  GoCommands and Command Line](https://learning.cyverse.org/ds/gocommands/)  
(*note*: CSR download this into ~/programs/)
2. In cyverse, navigate the folder you want contents uploaded to, select it, press 'Details' button and copy the 'Path' address (NOT the 'DE Link' address).
4. Use a command in the form of:  
`./gocmd iput -P <path-of-files-to-upload> <path-copied-from-cyverse>`  
For example, for one file:  
`./gocmd iput -P 4377294446.pdf /iplant/home/carolinarr/vis-sieve/Princeton_content`  


#### Go Command Examples

* view current configuration  
`./gocmd env`  
* from CSR's computer, uploaded all files named 'atlas*' to my *vis-sieve/Princeton_atlas* folder on cyverse  
`/Users/csimao/programs/gocmd put --progress atlas-* /iplant/home/carolinarr/vis-sieve/Princeton_atlas`  


