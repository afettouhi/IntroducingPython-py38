import imghdr
imghdr.what('oreilly.png')

from PIL import Image
img = Image.open('oreilly.png')
img.format

img.size

img.mode

img.show()

crop = (55, 70, 85, 100)
img2 = img.crop(crop)
img2.show()

img2.save('cropped.gif', 'GIF')
img3 = Image.open('cropped.gif')
img3.format

img3.size

mustache = Image.open('moustaches.png')
handlebar = mustache.crop((316, 282, 394, 310))
handlebar.size

img.paste(handlebar, (45, 90))
img.show()

from wand.image import Image
from wand.display import display

img = Image(filename='oreilly.png')
img.size

img.format

display(img)

import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open('oreilly.png')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()

import matplotlib.pyplot as plot
import matplotlib.image as image

img = image.imread('oreilly.png')
plot.imshow(img)
plot.show()
