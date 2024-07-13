import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect


class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Add Category')
        self.root.geometry('800x800')
        self.root.configure(bg="#A167A5")

        self.mainlabel=tkinter.Label(self.root,text="ADD CATEGORY",font=('arial',28,'bold'),bg="#A167A5",foreground="#0E273C")
        self.mainlabel.pack(pady=20)

        self.formframe=tkinter.Frame(self.root,bg="#A167A5")
        self.formframe.pack()
        h=('arial',15)

        self.name=tkinter.Label(self.formframe,text="Name",font=h,bg="#A167A5",foreground="#4A306D")
        self.name.grid(row=0,column=1,pady=20,padx=20)
        self.txt1=tkinter.Entry(self.formframe,width=30,relief=tkinter.SOLID)
        self.txt1.grid(row=0,column=2,pady=20)

        self.descp=tkinter.Label(self.formframe,text="Description",font=h,bg="#A167A5",foreground="#4A306D")
        self.descp.grid(row=1,column=1,pady=20,padx=20)
        self.txt2=tkinter.Entry(self.formframe,width=30,relief=tkinter.SOLID)
        self.txt2.grid(row=1,column=2,pady=20)

        self.btn=tkinter.Button(self.root,text="ADD",width=15,font=('arial',15),command=self.add,bg="#E8D7F1",foreground="#4A306D")
        self.btn.pack(pady=20)

        self.root.mainloop()

    def add(self):
        conn=Conect()
        cr = conn.cursor()
        n=self.txt1.get()
        d=self.txt2.get()
        if n=="" or d=="":
            msg.showinfo('',"All fields are Mandatory")
        else:
            q=f"insert into category values('{n}','{d}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo('',"Category Added", parent=self.root)



if __name__ == '__main__':
    x=main()