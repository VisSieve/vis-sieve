# Summary of directory contents

This script `get_pdf.py` is responsible for collecting the pdf that lies at the link or links within the `links` variable.

Honestly most of the script is a bit of a mystery to me, but can be looked at where I sourced it at https://stackoverflow.com/questions/68409249/how-to-download-pdf-files-with-playwright-python 

## Installation of playwright

The playwright program lets us perform the scrapes of pdfs that wget and curl would normally fail for

```
pip install pytest-playwright
playwright install
playwright install-deps
```

This is probably the main reason we want playwright, it simplifies the installation of the headless browsers that we need to use to download the pdfs.

## Next steps

After the pdfs have been collected then it's time to dump the figures from the pdf. `pdfimages` [https://en.wikipedia.org/wiki/Pdfimages](https://en.wikipedia.org/wiki/Pdfimages) is a great utility for this. 
## SBATCH processing

Note that this part requires a db file called publications.db (this requireent can be removed later on and made into a command line argument)

Within the current folder theres a number of files that are used for kicking off parallel pdf downloads
* sbatch_grabber.py
* multiprocess_grabber.py
* coordinator.sh
* grabbers.py

The idea is that `sbatch_grabber.py` receives a few command line arguments
* offset: means to skip a certain number of pdf ids from the beginning of the database list
* pdfs_per_task: means how many pdfs are downloaded by each parallel processing task
* tasks_total: this is how many parallel tasks are going to get started

This means that the total number of pdfs collected is `(pdfs_per_task * tasks_total)`. This script loops over the number of tasks and runs an sbatch command. If not running on a scheduled system this can be replaced with a multiprocessing pool that submits a subprocess command that runs the `grabber.py` in a shell environment provided the arguments.

To see a demonstration of this check out the file `multiprocess_grabber.py`

The result of this code in the folder is

```
content/
  {pub_id}/
    {pub_id}.pdf
    .
    .
    .
  {pub_id}/
    {pub_id}.pdf
```

### Preparing for image extraction

After collecting pdfs there are two remaining steps:
* creating a symbolic link folder that exposes the pdfs without the hierarchical structure provided by `grabbers.py`

`symlinker_pdfs.py` is the file that iterates over the results of the pdf grabbing. For each result in `content` that has a PDF, it creates a link under the folder `pdf_symlinks` using the publication id for the name of the file.
```
pdf_symlinks
  2340671844.pdf
  2399564276.pdf
  2510179618.pdf
  2516782548.pdf
  ...
```

## Image extraction

This part isn't handled by any of our specific scripts, we end up relying on pdffigures2 http://pdffigures2.allenai.org/

For this step we need the `pdffigures2.sif` container, and the following configuration steps.



```
# go get the pdffigures2 repo
git clone https://github.com/allenai/pdffigures2.git
```
then inside the container we are set to run
```
# we need to be inside the repo for things to work
cd pdffigures2
source "/root/.sdkman/bin/sdkman-init.sh"
sbt "runMain org.allenai.pdffigures2.FigureExtractorBatchCli $PWD/../pdf_symlinks -s stat_file.json -m $PWD/../pdf_symlinks/ -d $PWD/../pdf_symlinks/"
```

## Adding the pdf paths to the db file

Now that we are done with image extraction we need to update the database file. Note that this file assumes the database file is named `publications.db` but in the future this will be a command line argument that can be specified.

This script opens the `publications.db` file and iterates over the contents of the `pdf_symlinks` folder and for each `Figure*.png` found it adds that to the `figure` table of the database populating the paper_id, the figure id, the name of the figure and the weblink in cyverse for later presenting in visualizations.


