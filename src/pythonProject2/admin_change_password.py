import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect

class main:
    def __init__(self,email):
        self.root=Tk()
        self.root.title('Change')
        self.root.geometry('800x800')
        self.root.configure(bg="#A167A5")

        self.mainlabel=tkinter.Label(self.root,text="CHANGE PASSWORD",font=('arial',28,'bold'),bg="#A167A5",foreground="#0E273C")
        self.mainlabel.pack(pady=20)

        self.formframe=tkinter.Frame(self.root,bg="#A167A5")
        self.formframe.pack()
        h=('arial',15)

        self.email=tkinter.Label(self.formframe,text="Email",font=h,bg="#A167A5",foreground="#4A306D")
        self.email.grid(row=0,column=1,pady=20,padx=20)
        self.txt1=tkinter.Entry(self.formframe,width=30,relief=tkinter.SOLID)
        self.txt1.grid(row=0,column=2,pady=20)
        self.txt1.insert(0,email)
        self.txt1.configure(state='readonly')

        self.opass=tkinter.Label(self.formframe,text="Old Password",font=h,bg="#A167A5",foreground="#4A306D")
        self.opass.grid(row=1,column=1,pady=20,padx=20)
        self.txt2=tkinter.Entry(self.formframe,width=30,show='*',relief=tkinter.SOLID)
        self.txt2.grid(row=1,column=2,pady=20)

        self.npass=tkinter.Label(self.formframe,text="New Password",font=h,bg="#A167A5",foreground="#4A306D")
        self.npass.grid(row=2,column=1,pady=20,padx=20)
        self.txt3=tkinter.Entry(self.formframe,width=30,relief=tkinter.SOLID)
        self.txt3.grid(row=2,column=2,pady=20)

        self.btn=tkinter.Button(self.root,text="Change Password",font=h,width=20,command=self.change,bg="#E8D7F1",foreground="#4A306D")
        self.btn.pack(pady=20)

        self.root.mainloop()

    def change(self):
        conn=Conect()
        cr=conn.cursor()
        e=self.txt1.get()
        op=self.txt2.get()
        np=self.txt3.get()
        if e=="" or op=="" or np=="":
            msg.showinfo('',"All fields are mandatory",parent=self.root)
        else:
            q=f"select * from admin where email='{e}' and password='{op}'"
            cr.execute(q)
            data=cr.fetchall()
            print(data)
            if len(data)!=0:
                i=data[0][0]
                q1=f"update admin set password='{np}' where id='{i}'"
                print(q1)
                cr.execute(q1)
                conn.commit()
                msg.showinfo('',"Password Updated",parent=self.root)
            else:
                msg.showinfo('',"Wrong Email or Password",parent=self.root)

if __name__ == '__main__':
    x=main("emma@gmail.com")

