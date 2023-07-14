from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Encapsulation")
root.geometry("800x600")

label_name = Label(root, font=("Arial",50),bg="white")
label_name.place(relx=5,rely=4,anchor = CENTER)

class game:
    def __init__(self):
        self.__score = 0
    
    def updateGame(self):
        self.text = ["Black","Green","Red","Blue","Yellow","Pink"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","green","red","blue","yellow","pink"]
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_text]

obj1 = game()
btn1 = Button(root,text="Start",command=obj1.updateGame)
btn1.place(relx=0.5,rely=7,anchor = CENTER)

root.mainloop()