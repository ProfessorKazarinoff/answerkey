import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os
import img2pdf
from pdf_2_image import pdf_2_png

from os import listdir
from os.path import isfile, join


def write_over(png_image,text='Answer Key',left=1138,upper=10,right=1589,lower=101):

    font = ImageFont.truetype("Arial.ttf",54)
    img=Image.open(png_image)
    draw = ImageDraw.Draw(img)
    draw.rectangle([left, upper, right, lower], fill='white', outline='white')
    draw.text((1210, 30),text,fill='green',font=font)
    rename='name_removed-'+png_image
    img.save(rename)
    return

def write_pdf(image_list,pdf_name='name_removed.pdf'):
    with open(pdf_name, 'wb') as f:
        f.write(img2pdf.convert(image_list))


def main():
    pdf_2_png('scan.pdf')
    #write_over('temp/scan-0.png', 'WRITE_OVER')
    #write_over('temp/scan-0.png', 'WRITE_OVER')
    #write_pdf()
    #write_over('scan-2.png','Answer Key')
    cwd=os.getcwd()
    for filename in os.listdir(cwd):
         if filename.endswith(".png"):
             write_over(filename,'Answer Key')

    file_list=[]
    for filename in os.listdir(cwd):
        if filename.endswith(".png") and filename.startswith("name_removed-"):
            file_list.append(filename)
    write_pdf(file_list)


    print(file_list)

if __name__ == '__main__':
    main()



