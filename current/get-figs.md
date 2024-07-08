# Procedure to Use pdffigures2 Tool to Extract Figures from PDFs

Source: https://github.com/VisSieve/main/issues/17

**NOTE: Still in development. Update with final procedure.**


steps

retrieve and convert the pdffigures2 container to singularity on your hpc singularity build pdffigures2.sif docker://ghcr.io/devinbayly/pdffigures2
to run singularity shell pdffigures2.sif
in order to use the sbt program which was installed we need to source this installed file source "/root/.sdkman/bin/sdkman-init.sh"
then we need to access the cloned repo git clone https://github.com/allenai/pdffigures2.git
go inside the folder cd pdffigures2
then run the bulk pdf figure extractor
sbt "runMain org.allenai.pdffigures2.FigureExtractorBatchCli /path/to/pdf_directory/ -s stat_file.json -m /figure/image/output/prefix -d /figure/data/output/prefix"
in the above command the /path/to/pdf_directory is a folder with pdfs inside it, the /figure/image/output/prefix is whatever gets added to the fig1-1.png figures that follow a system like fig{page}-{number} for their identification.

the /figure/data/output/prefix is the prefix added to the json files that tell us about the figure or table that was extracted from the pdf
