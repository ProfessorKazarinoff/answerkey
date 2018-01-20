from wand.image import Image
import os

# Converting .pdf into .png
def convert_pdf (pdf_file):
    png_file=os.path.splitext(pdf_file)[0] + '.png'
    with Image(filename=pdf_file, resolution=200) as img:
        img.save(filename=png_file)

def main():
    convert_pdf('scan.pdf')

if __name__ == "__main__":
    main()