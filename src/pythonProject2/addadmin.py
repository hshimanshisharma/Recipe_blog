import tkinter
from tkinter import *
import tkinter.messagebox as msg

import Connection
from Connection import *
import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.bgcolour="#A167A5"
        self.root=Tk()
        self.root.title('Add Admin')
        self.root.geometry('800x800')
        self.root.configure(bg=self.bgcolour)

        self.mainlabel=tkinter.Label(self.root , text="Add Admin" , font=('ariel',28,'bold'),bg="#A167A5",foreground="#0E273C")
        self.mainlabel.pack(pady=20,ipadx=10,ipady=10)

        self.formFrame=tkinter.Frame(self.root,bg="#A167A5",width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.formFrame.pack_propagate(0)

        h=('ariel',15)

        self.name=tkinter.Label(self.formFrame, text="Name",font=h,bg="#A167A5",foreground="#4A306D")
        self.name.grid(row=0,column=1)
        self.txt1=tkinter.Entry(self.formFrame, width=30,relief=tkinter.SOLID)
        self.txt1.grid(row=0,column=2,pady=10)

        self.email = tkinter.Label(self.formFrame, text="Email", font=h,bg="#A167A5",foreground="#4A306D")
        self.email.grid(row=0, column=3,padx=10,pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, width=30,relief=tkinter.SOLID)
        self.txt2.grid(row=0, column=4,pady=10)

        self.password = tkinter.Label(self.formFrame, text="Password", font=h,bg="#A167A5",foreground="#4A306D")
        self.password.grid(row=1, column=1, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, width=30,relief=tkinter.SOLID)
        self.txt3.grid(row=1, column=2, pady=20)

        self.mobile = tkinter.Label(self.formFrame, text="Mobile", font=h,bg="#A167A5",foreground="#4A306D")
        self.mobile.grid(row=1, column=3, padx=20, pady=20)
        self.txt4 = tkinter.Entry(self.formFrame, width=30,relief=tkinter.SOLID)
        self.txt4.grid(row=1, column=4, pady=20)

        self.role = tkinter.Label(self.formFrame, text="Role", font=h,bg="#A167A5",foreground="#4A306D")
        self.role.grid(row=2, column=1, padx=20, pady=20)
        self.txt5 = ttk.Combobox(self.formFrame, values=('Super-Admin' ,'Admin'))
        self.txt5.grid(row=2, column=2, pady=20)

        self.btn=tkinter.Button(self.root,text='Submit',width=15,height=1,font=('ariel',15,'bold'),command=self.add,bg="#E8D7F1",foreground="#4A306D",activebackground="red",activeforeground="blue")
        self.btn.pack(pady=20)


        self.root.mainloop()


    def add(self):
        conn = Conect()
        cr = conn.cursor()

        self.n = self.txt1.get()
        self.e = self.txt2.get()
        self.p = self.txt3.get()
        self.m = self.txt4.get()
        self.r = self.txt5.get()

        if self.n == "" or self.e == "" or self.m == "" or self.r == "" or self.p == "":
            msg.showwarning('Warning',"All Fields are Mandatory",parent=self.root)
            # if Connection.Conect.verifyEmai(self.e)== False :
            #  msg.showwarning('',"Invalid email or Mobile Number", parent=self.root)
        else:
            if Connection.verifyEmail(self.e)=="Invalid" or Connection.verifyMobile(self.m)=="Invalid":
                msg.showwarning("","Invalid Email or Mobile")
            else:
                q = f"insert into admin values(null,'{self.n}' , '{self.e}', '{self.m}','{self.p}','{self.r}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo('Added'," Admin Added",parent=self.root)

if __name__ == '__main__':
    x=main()
