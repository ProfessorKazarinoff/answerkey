import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os
import shutil
from pdf_2_image import pdf_2_png
#from pdf_2_png import pdf_2_png
from img_2_pdf import img_2_pdf



#get import arguments

# pdf file with student name on it
# name of output pdf file


# also some how build in a temp dir for all of the .png's


def write_over(png_image,text='Answer Key',left=1138,upper=10,right=1589,lower=101):

    font = ImageFont.truetype("Arial.ttf",54)
    img=Image.open(png_image)
    draw = ImageDraw.Draw(img)
    draw.rectangle([left, upper, right, lower], fill='white', outline='white')
    draw.text((1210, 30),text,fill='green',font=font)
    rename='name_removed-'+png_image
    img.save(rename)
    return


def main():
    pdf_2_png('scan.pdf')

    cwd=os.getcwd()

    for filename in os.listdir(cwd):
         if filename.endswith(".png"):
             write_over(filename,'Answer Key')

    file_list=[]
    for filename in os.listdir(cwd):
        if filename.endswith(".png") and filename.startswith("name_removed-"):
            file_list.append(filename)


    print(file_list)

    #convert all .png's to .pdf's
    output_pdf_name = 'output8.pdf'
    img_2_pdf(file_list,output_pdf_name)

    print('Output pdf file: {}'.format(output_pdf_name))

    print('Moving .png files to the temp directory. If temp directory is not empty this may return an error. Move files of of temp dir to get rid of the error')
    tempdir = os.path.join(cwd,'temp')
    #shutil.rmtree(tempdir)
    os.mkdir(tempdir)
    for filename in os.listdir(cwd):
        if filename.endswith(".png"):
            full_file_name = os.path.join(cwd,filename)
            shutil.move(full_file_name, tempdir)

if __name__ == '__main__':
    main()



