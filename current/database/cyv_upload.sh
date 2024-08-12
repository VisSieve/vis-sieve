# Example script to upload files to cyverse database
# This example fits CSR's Cyverse Account

# STEPS

# 1. Install Go commands onto computer using instructions here:  
#[Transferring Data with  GoCommands and Command Line](https://learning.cyverse.org/ds/gocommands/)  
#(*note*: CSR download this into ~/programs/)

# 2. In cyverse, navigate the folder you want contents uploaded to, select it, press 'Details' button and copy the 'Path' address (NOT the 'DE Link' address).

# 3. Use a command such as the following 
/Users/csimao/programs/gocmd put --progress atlas-* /iplant/home/carolinarr/vis-sieve/Princeton_atlas
