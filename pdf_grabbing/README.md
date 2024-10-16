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
