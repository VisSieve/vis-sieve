import duckdb as db
import tqdm
from pathlib import Path
import requests as rq
import json

con = db.connect("publications_princeton.db")

# the first topic in the list has the highest score for each
# go through the work_topic table, and make a dictionary that holds the first entry of the work set

result = con.execute("SELECT * FROM work_topic;").fetchall()

primary_topic = {}
for row in result:
  unused_id,work_id,topic_id,score = row
  exists = primary_topic.get(work_id,None)
  if exists:
    continue
  primary_topic[work_id] = dict(score=score,topic_id=topic_id)

# go over the dictionary and add information to the work table in the form of the highest scoring topic id
try:
  con.execute("ALTER TABLE paper ADD COLUMN primary_topic_id BIGINT;")
except:
  # this already exists 
  print("primary topics column in table already")

for k in primary_topic:
  # use the update operation to change values in table
  # here we want to get the right row provided a work_id and set the primary topic id on it
  score,topic_id = primary_topic[k].values()
  con.execute(f"UPDATE paper SET primary_topic_id = {topic_id} WHERE id = {k}")

