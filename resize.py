from PIL import Image
import glob
image_list = []
i = 0
for filename in glob.glob('char/*.jpg'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
    im1 = im.resize((200,200))
    #im1.show()
    i += 1
    im1.save('%s.jpg'%i)
#print(image_list[1])

