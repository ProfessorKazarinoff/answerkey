from wand.image import Image
import os

def pdf_2_png(pdf_file, res=200):
    if not os.path.exists('temp'):
        os.makedirs('temp')
    png_filename=pdf_file.replace('.pdf', '.png')


    with Image(filename=pdf_file) as img:
        img.save(filename='temp/'+png_filename)

if __name__ == "__main__":
    pdf_2_png('scan.pdf')