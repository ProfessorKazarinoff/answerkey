import img2pdf
import PIL

def write_pdf(image_list,pdf_name='name_removed.pdf'):
    with open('aaa.pdf', 'wb') as f:
        f.write(img2pdf.convert(image_list))

if __name__ == '__main':
    write_pdf('name_removed-scan-0.png')