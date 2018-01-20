from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw



img=Image.open('scan-1.png')
print(img.size)
draw = ImageDraw.Draw(img)
draw.rectangle([1138, 10, 1589, 101], fill='white', outline='white')
img.save("w_rectangle.png")



