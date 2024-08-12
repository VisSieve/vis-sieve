# Wiki

This space is to provide resources for the project, such as important links, procedures, hints for other tools involved in each project stage, etc.

# Links

## GitHub

* Org: [https://github.com/VisSieve](https://github.com/VisSieve) (MAIN)

Older Repos  

* Devin’s https://github.com/DevinBayly/vis-seive/
* Carolina’s https://github.com/carolinarr/vis-sieve

## OpenAlex

+ [Documentation](https://docs.openalex.org/)
+ [Documentation - Topics](https://docs.openalex.org/api-entities/topics)
    + [Topics Paper](https://docs.google.com/document/d/1bDopkhuGieQ4F8gGNj7sEc8WSE8mvLZS/edit#heading=h.5w2tb5fcg77r) - contains diagram

## PDF Storage: cyverse 

[de.cyverse.org](https://de.cyverse.org/)

Devin's PDF Storage: [https://data.cyverse.org/dav-anon/iplant/home/baylyd/vis_sieve/](https://data.cyverse.org/dav-anon/iplant/home/baylyd/vis_sieve/)  
Carolina's PDF Storage: [https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_content](https://data.cyverse.org/dav-anon/iplant/home/carolinarr/vis-sieve/Princeton_content)


## Label Studio

[http://149.165.169.100:8080/](http://149.165.169.100:8080/)  
notes - CSR Labelstudio account reminder: c.roe email, low sec password

# Project Stages

1. get urls
2. get pdfs
3. get figs
4. label figs
4. visualization

## 1. Get URLS

[https://github.com/DevinBayly/vis-seive](https://github.com/DevinBayly/vis-seive)

## 2. Get PDFS

Cyverse Datastore link [https://data.cyverse.org/dav-anon/iplant/home/baylyd/vis_sieve/](https://data.cyverse.org/dav-anon/iplant/home/baylyd/vis_sieve/)

Example `python hear_me_ROR_script.py` run:

`python hear_me_ROR_script.py 2017 2018 --database ../database/publications.db --content_root ../database/content`

`python hear_me_ROR_script.py --help` to see all the options

## 3. Get Figs

Instead, now going to try pdffigures2.  
[!!! Insert Devin's container for pdffigures2.]

## 4. Label Figs

Originally tried LabelStudio:
[http://149.165.169.100:8080/user/login/](http://149.165.169.100:8080/user/login/)
go ahead and try to log in to and attempt to label a few things.


## 5. Visualization

### Observable Framework

more details to come, but [https://observablehq.com/framework/what-is-framework](https://observablehq.com/framework/what-is-framework) is a promising start. Note, it’s recommended to setup a code space from the vissieve repo. 

[https://devinbayly.observablehq.cloud/hello-duckdb/vissieve-test](https://devinbayly.observablehq.cloud/hello-duckdb/vissieve-test)

### Procedures

#### Docker Container + Reload  Setup Instructions

1. Follow "Setup docker container" instructions here: 
[https://github.com/DevinBayly/vis-sieve/tree/main/visualization](https://github.com/DevinBayly/vis-sieve/tree/main/visualization) 
BUT use this docker command instead:
**docker run -it --rm --mount type=bind,source="$(pwd)",target=/place -p 8080:8080 ghcr.io/devinbayly/vis_sieve_d3**
    1. Notes
        1. ghcr = github-container-registry
        2. See devin's repo to view what's installed in container when you open it: [https://github.com/DevinBayly/github-ci/blob/main/vis_sieve_d3](https://github.com/DevinBayly/github-ci/blob/main/vis_sieve_d3)
        3. *If* you open with docker command from vis-sieve repo (not updated command mentioned above), then you would run the following commands instead (once docker container opens):
            1. apt update
            2. apt install npm
                1. note: takes awhile
            3. npm install -g reload
                1. note: -g makes it global, so that any directory we go into we can run this reload command
2. Navigate to 'place' folder:
**cd place**
3. Run the reload command:
**reload**
4. Open browser and input URL:
**localhost:8080**
5. Change index.html file, and whenever you save, page should update
6. To exit:
    1. I think '**Ctrl + C**' to exit reload?
    2. I think '**exit**' to exit docker container?
    
    ## Database Information
    

[Database Information](database/database_information.md)

# Notion Shortcut

To indent bulleted list - Tab
To unindent bulleted list - Shift + Tab
