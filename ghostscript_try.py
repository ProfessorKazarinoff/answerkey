import sys
import locale
import ghostscript
# had to install ghostscript on laptop to make this work.

def pdf2jpeg(pdf_input_path, output_path):
    args = ["pdf2jpeg", # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=png16m",                       # png 24 bit rgb color
            "-r200",                                 # input rendering 200 dpi
            "-dDownScaleFactor=1",                   # make .png file 200 dpi as well
            "-sOutputFile=" + output_path,
            pdf_input_path]

    # arguments have to be bytes, encode them
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)

def main():
    pdf2jpeg('example.pdf','ghostscript_out_png200dpi.png')

if __name__ == '__main__':
    main()