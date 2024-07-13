from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import customtkinter
from gtts import gTTS
import playsound
import os
import threading


import Connection


class Main:
    def __init__(self):
        self.root = Toplevel()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text="Recipy List", font=('', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.recipyFrame = customtkinter.CTkScrollableFrame(self.root, width=self.root.winfo_screenwidth(),
                                                            height=self.root.winfo_screenheight())
        self.recipyFrame.pack(pady=10)

        self.recipyFrame.columnconfigure(0) #to stablize the width of column

        self.getRecipy()

        self.root.mainloop()

    def getRecipy(self):
        self.conn = Connection.Conect()
        self.cr = self.conn.cursor()

        q = f"SELECT * FROM recipe where image !=''"
        self.cr.execute(q)
        result = self.cr.fetchall()
        self.showRecipy(result)

    def showRecipy(self, recipes):
        for i in recipes:
            print(i[1])
            self.f = Frame(self.recipyFrame, width=self.root.winfo_screenwidth())
            self.f.pack(expand=True, fill='both')

            img = Image.open(fp=i[-1])
            img = img.resize((400,400))
            imgTk = ImageTk.PhotoImage(image=img)
            self.l = Label(self.f, image=imgTk)
            self.l.image=imgTk
            self.l.grid(row=0, column=0, pady=10, padx=10)

            self.f1 = Frame(self.f)
            self.f1.grid(row=0, column=1, pady=10, padx=10)

            self.nameLabel = Label(self.f1, text=i[1], font=('', 28))
            self.nameLabel.pack(pady=10)
            self.cat=Label(self.f1,text=i[5], font=('', 18))
            self.cat.pack(pady=10)
            self.duration = Label(self.f1, text=f"Duration - {i[3]} minutes", font=('', 12))
            self.duration.pack(pady=10)

            self.btn = Button(self.f1, text="View More", font=('', 14), command=
                              lambda r=i: self.playRecipy(r))
            self.btn.pack()

    def playRecipy(self, recipy):
        print(recipy)
        self.root1=Toplevel()
        self.root1.title('Recipe')
        self.root1.state('zoomed')

        self.lb=Label(self.root1,text=f"{recipy[1]}",font=('arial',28,'bold'))
        self.lb.pack(pady=20)

        self.recipyFrame1 = customtkinter.CTkScrollableFrame(self.root1, width=self.root1.winfo_screenwidth(),
                                                            height=self.root1.winfo_screenheight())
        self.recipyFrame1.pack(pady=10)
        self.recipyFrame1.columnconfigure(0)

        self.f2 = Frame(self.recipyFrame1, width=self.root.winfo_screenwidth())
        self.f2.pack(expand=True, fill='both')
        # self.mainlabel=Label(self.f2,text=f"{recipy[1]}",font=('arial',28,'bold'))
        # self.mainlabel.grid(row=0,column=1,pady=20)

        img = Image.open(fp=recipy[-1])
        img = img.resize((400, 400))
        imgTk = ImageTk.PhotoImage(image=img)
        self.l1 = Label(self.f2, image=imgTk)
        self.l1.image = imgTk
        self.l1.grid(row=0, column=0, pady=10, padx=10)

        self.f3 = Frame(self.f2)
        self.f3.grid(row=0, column=1, pady=10, padx=10)
        # self.d=Label(self.f3,text="Duration:",font=('', 17,'bold'))
        # self.d.grid(row=0,column=1)
        self.dur=Label(self.f3,text=f"Duration:{recipy[3]} minutes",font=('', 15))
        self.dur.pack(pady=20,anchor="w")

        self.ing=Label(self.f3,text="Ingredients:",font=('', 17,'bold'))
        self.ing.pack(anchor="w")

        tex=recipy[4]
        tex=tex.replace("/n",",")
        self.ingr=Label(self.f3,text=tex,font=('', 15))
        self.ingr.pack(anchor="w")

        self.des=Label(self.f3,text="Description:",font=('', 17,'bold'))
        self.des.pack(anchor="w")

        self.desp=Label(self.f3,text=f'{recipy[2]}',font=('', 15),wraplength=1000)
        self.desp.pack(anchor="w")

        self.bt=Button(self.f3,text="Play",width=15,font=('arial', 15, 'bold'),command=lambda: threading.Thread(target=self.play,args=[recipy]).start())
        self.bt.pack(pady=20)

        # self.f4 = Frame(self.recipyFrame1,width=self.root1.winfo_screenwidth())
        # self.f4.pack(expand=True, fill='both')
        # self.lb1=Label(self.f4,text="User ID: ",font=('',15))
        # self.lb1.grid(row=0,column=0,pady=5,padx=5)
        # self.txt1=Entry(self.f4,width=40)
        # self.txt1.grid(row=0,column=1)

        # self.lb5 = Label(self.f4, text=f"{self.name}", font=('', 19,'bold'))
        # self.lb5.grid(row=0, column=2, pady=10, padx=5)
        # self.txt5 = Entry(self.f4, width=40)
        # self.txt5.grid(row=0, column=1)

        # self.lb2 = Label(self.f4, text="Recipy ID: ", font=('', 15))
        # self.lb2.grid(row=0, column=2, pady=10, padx=10)
        # self.txt2 = Entry(self.f4, width=30)
        # self.txt2.grid(row=0, column=3)

        # self.lb3 = Label(self.f4, text="Rating:", font=('', 15))
    #     self.lb3.grid(row=1, column=1,  padx=10)
    #     self.txt3 = Entry(self.f4, width=40)
    #     self.txt3.grid(row=1, column=2)
    #
    #     self.lb4 = Label(self.f4, text="Add Comment", font=('', 15))
    #     self.lb4.grid(row=1, column=3,  padx=20)
    #     self.txt4 = Text(self.f4,height=5,width=30)
    #     self.txt4.grid(row=1, column=4)
    #     rid=recipy[0]
    #     self.bt1 = Button(self.f4, text="Submit", width=15, font=('arial', 15, 'bold'),command = lambda: self.add(rid))
    #     self.bt1.grid(row=2,column=2,pady=20)
    #
    #     self.root1.mainloop()
    #
    # def add(self,rid):
    #     print(rid)
    #     self.conn = Connection.Conect()
    #     self.cr = self.conn.cursor()
    #     self.ratings=self.txt3.get()
    #     print(self.ratings)
    #     self.rev=self.txt4.get('1.0','end-1c')
    #
    #     q = f"insert into review values(null,'{self.uid}','{rid}','{self.ratings}','{self.rev}')"
    #     print(q)
    #     self.cr.execute(q)
    #     self.conn.commit()
    #     self.cr.execute(q)
    #     result = self.cr.fetchall()
    #     self.showRecipy(result)
    #     msg.showinfo('',"Added")

    def play(self,recipy):
        lst= os.listdir('.')
        print(lst)
        if 'hello.mp3' in lst:
            os.remove('hello.mp3')

        obj = gTTS(text=recipy[2],lang='en')
        obj.save("hello.mp3")
        playsound.playsound('hello.mp3')
        os.remove('hello.mp3')




if __name__ == '__main__':
    x=Main()
