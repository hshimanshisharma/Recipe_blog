import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect
import user_dashboard
import Connection


class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Login')
        self.root.geometry('800x800')
        self.root.configure(bg="#DAB6FC")

        self.mainlabel=tkinter.Label(self.root,text="USER LOGIN",font=('arial',28,'bold'),bg="#DAB6FC")
        self.mainlabel.pack(pady = 20)

        self.formFrame = tkinter.Frame(self.root,bg="#DAB6FC")
        self.formFrame.pack()
        h = ('arial', 15)

        self.email=tkinter.Label(self.formFrame,text="Email",font=h,bg="#DAB6FC")
        self.email.grid(row=0,column=1,padx=20,pady=20)
        self.txt1=tkinter.Entry(self.formFrame,width=30,relief=tkinter.SOLID)
        self.txt1.grid(row=0,column=2,pady=20)

        self.password=tkinter.Label(self.formFrame,text="Password",font=h,bg="#DAB6FC")
        self.password.grid(row=1,column=1,pady=20,padx=20)
        self.txt2=tkinter.Entry(self.formFrame,width=30,show='*',relief=tkinter.SOLID)
        self.txt2.grid(row=1,column=2,pady=20)

        self.btn=tkinter.Button(self.root,text="Login",font=('arial',15),width=15,command=self.login,bg="#8895B3")
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
            q=f"select * from user where email='{e}' and password='{p}'"
            self.cr.execute(q)
            result=self.cr.fetchall()
            print(result)
            if len(result)==0:
                msg.showinfo('',"Login Fail")
            else:
                # msg.showinfo('',"Login Successful")
                if Connection.verifyEmail(e) == "Invalid":
                    msg.showwarning("", "Invalid Email")
                else:
                    id=result[0][0]
                    em=result[0][2]
                    name=result[0][1]
                    user_dashboard.main(id,em,name)

if __name__ == '__main__':
    x=main()

