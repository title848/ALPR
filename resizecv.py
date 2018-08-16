from PIL import Image

basewidth = 300
img = Image.open('1.JPEG')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((1000,500), Image.NEAREST)
img.save('sompic.jpg') 