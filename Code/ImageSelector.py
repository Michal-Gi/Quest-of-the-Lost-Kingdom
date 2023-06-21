from tkinter import Tk, Label, Button
from PIL import ImageTk, Image


class ImageSelector:
    """
        Klasa ImageSelector umożliwia użytkownikowi wybór obrazu za pomocą interfejsu graficznego.

        Atrybuty:
            master (Tk): Główne okno aplikacji Tkinter.
            avatar (str): Wybrany avatar gracza.
            image1 (ImageTk.PhotoImage): Obrazek dostępny do wyboru.
            image2 (ImageTk.PhotoImage): Drugi obrazek dostępny do wyboru.
            label1 (Label): Etykieta zawierająca pierwszy obrazek.
            label2 (Label): Etykieta zawierająca drugi obrazek.

        Metody:
            __init__(self, master): Inicjalizuje obiekt ImageSelector, ładuje obrazki i wyświetla je w etykietach.
            select_image1(self, event): Wybiera pierwszy obrazek jako avatar gracza, wyświetla komunikat i zamyka okno.
            select_image2(self, event): Wybiera drugi obrazek jako avatar gracza, wyświetla komunikat i zamyka okno.
        """
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



