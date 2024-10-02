#!/bin/bash

# Script to(1) upload files to cyverse database, adn (2) generate list of links to file locations. 

# This example fits CSR's Cyverse Account
# Created by: Carolina Roe-Raymond (c.roe-raymond@princeton.edu)

#*********************************************
# BACKGROUND / SETUP
#*********************************************

# 1. Install Go commands onto computer using instructions here:  
#[Transferring Data with  GoCommands and Command Line](https://learning.cyverse.org/ds/gocommands/)  
#(*note*: CSR download this into ~/programs/)

# 2. In [cyverse's Discovery Environment](https://de.cyverse.org/), login and navigate the folder you want contents uploaded to, select it, 
# press 'Details' button and copy the 'Path' address (NOT the 'DE Link' address).

# 3. To place files on cyverse, we'll use a command that fits the following structure
<path-to-gocmd> put --progress <file-names> <cyverse path>

# For example, to place all images that start with 'atlas-' onto cyverse for CSR:
# /Users/csimao/programs/gocmd put --progress atlas-* /iplant/home/carolinarr/vis-sieve/Princeton_atlas

#*********************************************
# CODE
#*********************************************

# (1) Upload files to cyverse
# ****************************
# Navigate to folder with pdf content
cd content # assumes you've started in 'current/' folder

# Update variables as needed 
my_gocmd="/Users/csimao/programs/gocmd" # location of gocmd install
file="*" # regex expression for desired files
cyverse_path="/iplant/home/carolinarr/vis-sieve/testing" # cyverse 'Path' address (copied from de.cyverse.org)

# Upload files to cyvserve
$my_gocmd put --progress $file $cyverse_path

echo "Processing complete. Files have been uploaded to cyverse at $cyverse_path location."

# Generate list of file locations
# ****************************
# Save list of directory names on cyverse to a csv file
# (needed when updating 'papers' table in DuckDb database)

# specify file nameand location, including today's date
today=$(date +"%Y-%m-%d_%H-%M-%S")
filename="../database/data/cyverse_pdfspaths_$today"

# save list of directory contents to text file
# *********
/Users/csimao/programs/gocmd ls $cyverse_path > $filename.txt

# format raw list
# *********

# Replace '  C- ' at start of each line with 'https://data.cyverse.org/dav-anon'
# Saved to temp file, then temp file replaces orig file)
sed 's/^  C- /https:\/\/data.cyverse.org\/dav-anon/' $filename.txt > temp_file && mv temp_file $filename.txt

# create a second column of data with paper's id, and convert to .csv file

input_file=$filename.txt
output_file=$filename.csv

# Clear the output file if it exists
> $output_file

# Process each line of the input file
while IFS= read -r line
do
    # Extract the part after the last '/'
    extracted=$(echo "$line" | awk -F'/' '{print $NF}')
    
    # Append the extracted part to the end of the line with a ', ' before it
    modified_line="$line, $extracted"
    
    # Write the modified line to the output file
    echo "$modified_line" >> $output_file
done < "$input_file"

echo "Processing complete. Modified lines have been saved to $output_file."
