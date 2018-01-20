from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os
import shutil
from pdf_2_image import pdf_2_png
from gooey import Gooey
from gooey import GooeyParser
#from pdf_2_png import pdf_2_png
from img_2_pdf import img_2_pdf



#get import arguments

# pdf file with student name on it
# name of output pdf file
# also some how build in a temp dir for all of the .png's


def write_over(png_image,text='Answer Key',left=1138,upper=10,right=1589,lower=101):

    font = ImageFont.truetype("arialbd.ttf",54)
    #font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 54)
    #font = ImageFont.truetype("arial", 54)
    img=Image.open(png_image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.rectangle([left, upper, right, lower], fill='white', outline='white')
    draw.text((1210, 30),text,fill=(0, 128, 0),font=font)
    rename='name_removed-'+png_image
    img.save(rename)
    return

@Gooey
def main():
    parser = GooeyParser(description="Removing Name from student HW and stamping Answer Key GUI App!")
    parser.add_argument('scanned_pdf', help="Select the .pdf scan you want to remove the student name from", widget='FileChooser')
    parser.add_argument('output_pdf', help="Name your output .pdf file. Include the .pdf extension in the file name", widget='TextField')
    parser.add_argument('temp_dir', help="Type name of temp dir you want the created .png's to be stored in", widget='TextField')
    args = vars(parser.parse_args())

    scanned_pdf = (args["scanned_pdf"])
    output_pdf = (args["output_pdf"])
    temp_dir_name = (args["temp_dir"])

    pdf_2_png(scanned_pdf)

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
    if not output_pdf.endswith(".pdf"):
        output_pdf += ".pdf"
    output_pdf_name = output_pdf
    img_2_pdf(file_list,output_pdf_name)

    print('Output pdf file: {}'.format(output_pdf_name))

    print('Moving .png files to the {} directory'.format(temp_dir_name))
    tempdir = os.path.join(cwd,temp_dir_name)
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    for filename in os.listdir(cwd):
        if filename.endswith(".png"):
            full_file_name = os.path.join(cwd,filename)
            shutil.move(full_file_name, tempdir)

if __name__ == '__main__':
    main()



