#from wand.image import Image
import os
from pathlib import Path, PurePath
# C:\Users\peter.kazarinoff\Documents\ImageMagick

from pdf2image import convert_from_path

from pdf2image.exceptions import (
PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError, PopplerNotInstalledError
)

#p = PurePath('C:\\Users\\peter.kazarinoff\\Documents\\ImageMagick')
#os.environ['MAGICK_HOME'] = r"C:\Users\peter.kazarinoff\Documents\ImageMagick"

def pdf_2_png(pdf_file, res=200):
    images = convert_from_path(pdf_file,dpi=res)
    for i, image in enumerate(images):
        fname = "image"+str(i)+".png"
        image.save(fname, "PNG")

# def pdf_2_png(pdf_file, res=200):
#     if not os.path.exists('temp'):
#         os.makedirs('temp')
#     png_filename=pdf_file.replace('.pdf', '.png')
#     # Converting first page into JPG
#
#     with Image(filename=pdf_file, resolution=res) as img:
#         img.save(filename=png_filename)

if __name__ == "__main__":
    pdf_2_png('scan.pdf')