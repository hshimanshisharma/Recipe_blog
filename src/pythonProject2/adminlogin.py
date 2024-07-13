import tkinter
from tkinter import *
import tkinter.messagebox as msg
import Connection
import admindashboard
from Connection import Conect
import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Login')
        self.root.geometry('600x600')
        self.root.configure(bg="#A167A5")

        self.mainlabel=tkinter.Label(self.root,text="ADMIN LOGIN",font=('arial',28,'bold'),bg="#A167A5",foreground="#0E273C")
        self.mainlabel.pack(pady = 20,ipady=10)

        self.formFrame = tkinter.Frame(self.root,bg="#A167A5")
        self.formFrame.pack()
        h = ('ariel', 15)

        self.email=tkinter.Label(self.formFrame,text="Email",font=h,bg="#A167A5",foreground="#4A306D")
        self.email.grid(row=0,column=1,padx=20,pady=20)
        self.txt1=tkinter.Entry(self.formFrame,width=30,relief=tkinter.SOLID)
        self.txt1.grid(row=0,column=2,pady=20)

        self.password=tkinter.Label(self.formFrame,text="Password",font=h,bg="#A167A5",foreground="#4A306D")
        self.password.grid(row=1,column=1,pady=20,padx=20)
        self.txt2=tkinter.Entry(self.formFrame,width=30,show='*',relief=tkinter.SOLID)
        self.txt2.grid(row=1,column=2,pady=20)

        self.btn=tkinter.Button(self.root,text="Login",font=('arial',15),width=15,command=self.login,bg="#E8D7F1",foreground="#4A306D")
        self.btn.pack()

        self.root.mainloop()

    def login(self):
        self.conn = Conect()
        self.cr = self.conn.cursor()
        e=self.txt1.get()
        p=self.txt2.get()
        if e=="" or p=="":
            msg.showinfo('',"All fields are mandatory")
        else:
            q=f"select * from admin where email='{e}' and password='{p}'"
            self.cr.execute(q)
            result=self.cr.fetchall()
            print(result)
            if len(result)==0:
                msg.showinfo('',"Login Fail")
            else:
                if Connection.verifyEmail(self.e) == "Invalid":
                    msg.showwarning("", "Invalid Email")
                else:
                    id=result[0][0]
                    name=result[0][1]
                    email=result[0][2]
                    role=result[0][5]
                    admindashboard.Main(id,name,email,role)

if __name__ == '__main__':
    x=main()

