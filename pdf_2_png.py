#from wand.image import Image
import os
from pdf2image import convert_from_path

from pdf2image.exceptions import (
PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError, PopplerNotInstalledError
)

def pdf_2_png(pdf_file, res=200):
    images = convert_from_path(pdf_file,dpi=res,output_folder='temp')
    for i, image in enumerate(images):
        fname = "image"+str(i)+".png"
        image.save(fname, "PNG")
    # if not os.path.exists('temp'):
    #     os.makedirs('temp')
    # png_filename=pdf_file.replace('.pdf', '.png')
    #
    #
    # with Image(filename=pdf_file) as img:
    #     img.save(filename='temp/'+png_filename)

if __name__ == "__main__":
    pdf_2_png('scan.pdf')