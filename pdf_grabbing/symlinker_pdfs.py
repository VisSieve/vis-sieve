from pathlib import Path

# gives back a generator
pdfs = sorted(Path("content").glob("*/*.pdf")) 
# "content/1508049984/1508049984.pdf"
# now make a new folder
# this is where the symlinks go
out = Path("pdf_symlinks")
out.mkdir(exists_ok = True) 

# now we will make actual symlinks for each file
for pdf in pdfs:
  symlink_path = Path(f"{out}/{pdf.stem}")
  if symlink_path.is_symlink():
    continue

  symlink_path.symlink_to(pdf.absolute())
