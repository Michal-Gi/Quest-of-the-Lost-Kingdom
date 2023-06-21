from tkinter import Tk, Label, Button
from PIL import ImageTk, Image


class ImageSelector:
    def __init__(self, master):
        self.master = master
        self.avatar = ''
        master.title("Select an Image")

        self.image1 = ImageTk.PhotoImage(Image.open('../Assets/Characters/Player/idle1.png'))
        self.image2 = ImageTk.PhotoImage(Image.open('../Assets/Characters/Player/ridle1.png'))

        self.label1 = Label(master, image=self.image1)
        self.label1.bind('<Button-1>', self.select_image1)
        self.label1.pack(side="left")

        self.label2 = Label(master, image=self.image2)
        self.label2.bind('<Button-1>', self.select_image2)
        self.label2.pack(side="right")

    def select_image1(self, event):
        print("Image 1 was selected")
        self.avatar = ''
        self.master.destroy()

    def select_image2(self, event):
        print("Image 2 was selected")
        self.avatar = 'r'
        self.master.destroy()



