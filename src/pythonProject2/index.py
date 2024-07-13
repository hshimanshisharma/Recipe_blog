import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect
import Userlogin
import adminlogin

class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Recipes')
        self.root.geometry('600x600')
        self.root.configure(bg="#005E7C")

        self.mainlabel=tkinter.Label(self.root,text="Recipe System",font=('arial',28,'bold'))
        self.mainlabel.pack(pady=20)

        self.formframe = tkinter.Frame(self.root, bg="#005E7C")
        self.formframe.pack()

        self.btn = tkinter.Button(self.formframe, text="Admin", width=15, font=('arial',17), command=lambda:adminlogin.main(), bg="#0094C6",
                                  foreground="white")
        self.btn.grid(row=0,column=1,pady=20,padx=20)

        self.btn1 = tkinter.Button(self.formframe, text="User", width=15, font=('arial',17), command=lambda:Userlogin.main(), bg="#0094C6",
                                  foreground="white")
        self.btn1.grid(row=0,column=2,pady=20,padx=20)

        self.root.mainloop()

x=main()