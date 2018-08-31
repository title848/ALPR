from PIL import Image
import glob
image_list = []
i = 0
for filename in glob.glob('000/*.bmp'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
    im1 = im.resize((20,20))
    #im1.show()
    i += 1
    im1.save('000/%s.bmp'%i)
#print(image_list[1])

