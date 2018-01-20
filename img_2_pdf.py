import img2pdf
"""

converts an image (.jpg or .png) to a .pdf file
# see docs: https://pypi.python.org/pypi/img2pdf

$ pip install img2pdf

"""

def img_2_pdf(image_list, pdf_file_name='output.pdf'):

    with open(pdf_file_name,"wb") as f:
        f.write(img2pdf.convert(image_list))

def main():
    img_list = ['name_removed-scan-0.png', 'name_removed-scan-1.png']
    output_pdf = 'output_from_img_2_pdf.pdf'
    img_2_pdf(img_list,output_pdf)


if __name__ == '__main__':
    main()