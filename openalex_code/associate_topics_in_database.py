import duckdb as db
import tqdm
from pathlib import Path
import requests as rq
import json

con = db.connect("publications_princeton.db")

# use the work id to get the original result from open alex again
# then we need to construct a dictionary of all the unique combos of topics 
# then we will create the new tables that have information in them that allow for relating works to topics

#works = con.sql("SELECT id FROM paper").fetchall()
#print(works)
## make requests for each work to get back the data that has the topics in it
#information = {}
#for fetch_res in tqdm.tqdm(works):
#  work = fetch_res[0]
#  res = rq.get(f"https://api.openalex.org/works/W{work}").json()
#  topics = res["topics"]
#  keywords = res["keywords"]
#  information[work] = {"topics":topics,"keywords":keywords}
#
#Path("temp_results.json").write_text(json.dumps(information))





# this is the table that holds the unique topics
try:
  con.execute("""
  DROP TABLE IF EXISTS topic;
  DROP TABLE IF EXISTS work_topic;
  DROP TABLE IF EXISTS keyword;
  DROP TABLE IF EXISTS work_keyword;
  """)
  con.execute("""
  CREATE TABLE topic (
  id BIGINT,
  name VARCHAR(150),
  subfield VARCHAR(150),
  field VARCHAR(150),
  domain VARCHAR(150)
  );
  """)
  # this is the table that will hold the pairing between the work and the topics
  con.execute("""
  CREATE TABLE work_topic (
  id BIGINT,
  work_id BIGINT,
  topic_id BIGINT,
  score DOUBLE,
  );
  """)

  # now we will do the same thing for the keywords
  con.execute("""
  CREATE TABLE keyword (
  id BIGINT,
  keyword VARCHAR(150)
  );
  """)
  # now we make a pairing table that will map to the individual keywords
  con.execute("""
  CREATE TABLE work_keyword (
  id BIGINT,
  work_id BIGINT,
  keyword_id BIGINT,
  score DOUBLE
  );
  """)
except Exception as e:
  print("had slight prob, no biggie")
data = json.loads(Path("temp_results.json").read_text())

# now we will associate the information in the new tables for the database
# step 1 is to get a de duplicated list of the keywords

dedup_keywords = {}



# same thing for the topics, we can rely on the topic not coming up in other subfields though, so we can essentially map just on that 
dedup_topics = {}

for work_topic_id,work_id in tqdm.tqdm(enumerate(data)):
  # attempt to add topic
  work_data = data[work_id]
  topics = work_data["topics"]
  keywords = work_data["keywords"]
  for topic in topics:
    name= topic["display_name"].replace("'","")
    subfield = topic["subfield"]["display_name"].replace("'","")
    field = topic["field"]["display_name"].replace("'","")
    domain= topic["domain"]["display_name"].replace("'","")
    score = topic["score"]
    next_topic_id = con.sql("SELECT COUNT(id) FROM topic;").fetchall()[0][0] +1
    # check if topic is in the dictionary of topics
    topic_exists = dedup_topics.get(name,-1)
    # if not we later store its id
    if topic_exists==-1: 
      con.execute(f"INSERT INTO topic VALUES ({next_topic_id}, '{name}', '{subfield}', '{field}', '{domain}');")
      assignment_topic_id = next_topic_id
      dedup_topics[name] = assignment_topic_id
      # this happens when the data is in the table already, 
      # in this case we want to retrieve the original id value for filling out the work_topic table
    else:
      assignment_topic_id = topic_exists
    # now we will add the work_topic entry
    try:
      con.execute(f"INSERT INTO work_topic VALUES ( {work_topic_id}, {work_id}, {assignment_topic_id}, {score});")
    except db.ConstraintException:
      pass
  for keyword in keywords:
    name= keyword["display_name"].replace("'","")
    score = keyword["score"]
    next_keyword_id = con.sql("SELECT COUNT(id) FROM keyword;").fetchall()[0][0] +1
    keyword_exists = dedup_keywords.get(name,-1)
    if keyword_exists ==-1:
      con.execute(f"INSERT INTO keyword VALUES ({next_topic_id}, '{name}');")
      assignment_keyword_id = next_keyword_id
      dedup_keywords[name] = assignment_keyword_id
    else:
      # this happens when the data is in the table already, 
      # in this case we want to retrieve the original id value for filling out the work_topic table

      assignment_keyword_id = keyword_exists
    # now we will add the work_topic entry
    try:
      con.execute(f"INSERT INTO work_keyword VALUES ( {work_topic_id}, {work_id}, {assignment_keyword_id}, {score});")
    except db.ConstraintException:
      pass

    

