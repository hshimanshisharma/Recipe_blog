import tkinter
from tkinter import *
import tkinter.messagebox as msg
import Connection
import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Add')
        self.root.geometry('800x800')
        self.root.configure(bg="#DAB6FC")

        self.mainlabel=tkinter.Label(self.root,text="ADD USER",font=('arial',28,'bold'),bg="#DAB6FC",foreground="black")
        self.mainlabel.pack(pady=20)

        self.formframe=tkinter.Frame(self.root,bg="#DAB6FC")
        self.formframe.pack()
        h=('arial',15)

        self.name = tkinter.Label(self.formframe, text="NAME", font=h,bg="#DAB6FC",foreground="black")
        self.name.grid(row=0, column=1, padx=20, pady=20)
        self.txt2 = tkinter.Entry(self.formframe, width=30,relief=tkinter.SOLID)
        self.txt2.grid(row=0, column=2, pady=20)

        self.email = tkinter.Label(self.formframe, text="EMAIL", font=h,bg="#DAB6FC",foreground="black")
        self.email.grid(row=0, column=3, padx=20, pady=20)
        self.txt3 = tkinter.Entry(self.formframe, width=30,relief=tkinter.SOLID)
        self.txt3.grid(row=0, column=4, pady=20)

        self.mobile = tkinter.Label(self.formframe, text="MOBILE", font=h,bg="#DAB6FC",foreground="black")
        self.mobile.grid(row=1, column=1, padx=20, pady=20)
        self.txt4 = tkinter.Entry(self.formframe, width=30,relief=tkinter.SOLID)
        self.txt4.grid(row=1, column=2, pady=20)

        self.password = tkinter.Label(self.formframe, text="PASSWORD", font=h,bg="#DAB6FC",foreground="black")
        self.password.grid(row=1, column=3, padx=20, pady=20)
        self.txt5 = tkinter.Entry(self.formframe, width=30,relief=tkinter.SOLID)
        self.txt5.grid(row=1, column=4, pady=20)

        self.gender = tkinter.Label(self.formframe, text="GENDER", font=h,bg="#DAB6FC",foreground="black")
        self.gender.grid(row=2, column=1, padx=20, pady=20)
        self.txt6 = ttk.Combobox(self.formframe, values=('MALE', 'FEMALE','OTHER'))
        self.txt6.grid(row=2, column=2, pady=20)

        self.address = tkinter.Label(self.formframe, text="ADDRESS", font=h,bg="#DAB6FC",foreground="black")
        self.address.grid(row=2, column=3, padx=20, pady=20)
        self.txt7 = tkinter.Entry(self.formframe, width=30,relief=tkinter.SOLID)
        self.txt7.grid(row=2, column=4, pady=20)

        self.btn=tkinter.Button(self.root,text="SIGNUP",width=20,font=h,command=self.signup,bg="#8895B3",foreground="black")
        self.btn.pack(pady=20)

        self.root.mainloop()

    def signup(self):
        conn=Conect()
        cr=conn.cursor()
        n=self.txt2.get()
        e=self.txt3.get()
        m=self.txt4.get()
        p=self.txt5.get()
        g=self.txt6.get()
        a=self.txt7.get()

        if n == "" or e == "" or m == "" or g == "" or p == "" or a=="":
            msg.showwarning('Warning', "All Fields are Mandatory",parent=self.root)
        else:
            if Connection.verifyEmail(self.e) == "Invalid" or Connection.verifyMobile(self.m) == "Invalid":
                msg.showwarning("", "Invalid Email or Mobile")
            else:
                q = f"insert into user values(null,'{n}' , '{e}', '{m}','{p}','{g}','{a}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo('Added', " Account Created", parent=self.root)


if __name__ == '__main__':
    x=main()

