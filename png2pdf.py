import img2pdf

# see docs: https://pypi.python.org/pypi/img2pdf

# multiple inputs (variant 2)
with open("name1.pdf","wb") as f:
    f.write(img2pdf.convert(["scan-0.png", "scan-1.png"]))