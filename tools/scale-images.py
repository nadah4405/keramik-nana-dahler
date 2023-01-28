import os
from pathlib import Path
from PIL import Image

in_path = "bilder-website"
out_path = "bilder-website-scaled"

size = 1200, 800

if __name__ == "__main__":
    result = list(Path(in_path).rglob("*.[jJ][pP][gG]"))
    for infile in result:
        outfile = Path(out_path).joinpath(*infile.parts[1:])
        outdir = Path(out_path).joinpath(*infile.parts[1:-1])
        
        print(infile.__str__() + " -> " + outfile.__str__())
        os.makedirs(outdir, exist_ok = True) 
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, "JPEG", quality=90)
