from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/viewer_icon.png')

my_img = ImageTk.PhotoImage(Image.open('images/ladybird.png'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()