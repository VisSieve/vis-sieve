import subprocess as sp
import logging
from pathlib import Path
import argparse
import multiprocessing as mp

parser = argparse.ArgumentParser()
parser.add_argument("offset")
parser.add_argument("pdfs_per_task")
parser.add_argument("tasks_total")
args = parser.parse_args()
logger = logging.getLogger(__name__)

logging.basicConfig(filename='myapp.log', level=logging.INFO)
offset = int(args.offset)
number_pdfs_per_task = int(args.pdfs_per_task)
tasks = int(args.tasks_total)


def submit_pdf_grab_request(args):
  #unpack the args 
  row_start,row_end = args
  # run grabbers.py in the playwright sif environment
  sp.run(f"singularity exec playwright.sif grabbers.py {row_start} {row_end} publications.db".split(" "))

arg_list = []

for i in range(tasks):
  row_start =i*number_pdfs_per_task + offset
  row_end = (i+1)*number_pdfs_per_task + offset
  arg_list.append([row_start,row_end])

cores = 8
with multiprocessing.Pool(cores) as pool:
  pool.map(submit_pdf_grab_request,arg_list)
