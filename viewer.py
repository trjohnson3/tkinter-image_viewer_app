from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/viewer_icon.png')

my_img1 = ImageTk.PhotoImage(Image.open('images/ladybird.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/sunset.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/ganesha.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/xmas.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/pie_chart.png'))

img_number = 0

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    global img_number
    if img_number == 4:
        img_number = 0
    else:
        img_number += 1

    global my_label
    my_label.grid_forget()
    my_label = Label(image=image_list[img_number])
    my_label.grid(row=0, column=0, columnspan=3)


def back():
    global img_number
    if img_number == 0:
        img_number = 4
    else:
        img_number -= 1

    global my_label
    my_label.grid_forget()
    my_label = Label(image=image_list[img_number])
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", width=28, command=back)
button_exit = Button(root, text="Exit Program", width=28, command=root.quit)
button_forward = Button(root, text=">>", width=28, command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()