import tkinter
from tkinter import *
import tkinter.messagebox as msg

import Connection
from Connection import Conect
import tkinter.ttk as ttk

class Main:
    def __init__(self):
        self.root=Tk()
        self.root.title('View Admin')
        self.root.state('zoomed')

        self.lb= tkinter.Label(self.root, text='VIEW ADMIN', font=('arial',28,'bold'),foreground="#A80CB3")
        self.lb.pack(pady=20)

        self.formframe=tkinter.Frame(self.root)
        self.formframe.pack()

        h = ('arial', 15)
        self.lb1=tkinter.Label(self.formframe,text="Search",font=('arial', 15,'bold'),foreground="#48284A")
        self.lb1.grid(row=0,column=0)
        self.txt=tkinter.Entry(self.formframe,width=30)
        self.txt.grid(row=0,column=1, padx=20)
        self.btn1=tkinter.Button(self.formframe,text="Search",font=('arial',10),command=self.search,bg="#9E7AA1")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial',10),command=self.getvalues,bg="#9E7AA1")
        self.btn1.grid(row=0,column=2)
        self.btn2.grid(row=0,column=3, padx=20)

        self.admintable=ttk.Treeview(self.root,columns=('id','name','email','mobile','role'))
        self.admintable.pack(pady=10,expand=True,fill='both')
        self.btn = tkinter.Button(self.root,text="DELETE",width = 15,command=self.delete,bg="#9E7AA1")
        self.btn.pack(pady=10)
        self.admintable.heading('id',text="ID")
        self.admintable.heading('name', text="NAME")
        self.admintable.heading('email', text="EMAIL")
        self.admintable.heading('mobile', text="MOBILE")
        self.admintable.heading('role', text="ROLE")
        self.admintable['show']='headings'

        self.admintable.bind("<Double-1>", self.open)

        self.getvalues()

        style=ttk.Style()
        style.configure('Treeview',font=('arial',18),rowheight=40,foreground="white",background="#916C80")
        style.configure('Treeview.Heading',font=('arial',25,'bold'),rowheight=40,foreground="#48284A")

        self.root.mainloop()

    def getvalues(self):
        self.conn=Connection.Conect()
        self.cr=self.conn.cursor()
        q="select id,name,email,mobile,role from admin"
        self.cr.execute(q)

        data=self.cr.fetchall()
        for row in self.admintable.get_children():
            self.admintable.delete(row)
        c=0
        for i in data:
            self.admintable.insert('',index=c , value=i)
            c+=1

    def search(self):
        self.conn=Connection.Conect()
        self.cr=self.conn.cursor()
        s=self.txt.get()
        q=f"select * from admin where name like '%{s}%' or email like '%{s}%' or mobile like '%{s}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()

        for row in self.admintable.get_children():
            self.admintable.delete(row)
        c=0
        for i in data:
            self.admintable.insert('',index=c,value=i)
            c+=1

    def delete(self):
        rowid = self.admintable.selection()
        if len(rowid)==0:
            msg.showinfo('',"Select a row!")
        elif len(rowid)>1:
            msg.showinfo('',"Please select only one row at a time!!")
        else:
            items=self.admintable.item(rowid[0])
            data=items['values']
            q=f"delete from admin where id='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo('',"Row Deleted")

    def open(self,e):
        data=self.admintable.item(self.admintable.selection()[0])['values']
        self.root1=Toplevel()
        self.root1.title('Update')
        self.root1.geometry('800x800')

        self.lb2=Label(self.root1,text="UPDATE ADMIN",font=('ariel',28))
        self.lb2.pack(pady=20)

        self.formFrame1 = Frame(self.root1)
        self.formFrame1.pack()

        h = ('ariel', 15)

        self.id = Label(self.formFrame1, text="ID", font=h)
        self.id.grid(row=0, column=1, padx=20, pady=20)
        self.txt6 = Entry(self.formFrame1, width=30)
        self.txt6.grid(row=0, column=2, pady=20)
        self.txt6.insert(0,data[0])
        self.txt6.configure(state='readonly')

        self.name =Label(self.formFrame1, text="Name", font=h)
        self.name.grid(row=0, column=3, padx=20, pady=20)
        self.txt1 =Entry(self.formFrame1, width=30)
        self.txt1.grid(row=0, column=4, pady=20)
        self.txt1.insert(0,data[1])

        self.email = Label(self.formFrame1, text="Email", font=h)
        self.email.grid(row=1, column=1, padx=20, pady=20)
        self.txt2 = Entry(self.formFrame1, width=30)
        self.txt2.grid(row=1, column=2, pady=20)
        self.txt2.insert(0, data[2])

        self.mobile = Label(self.formFrame1, text="Mobile", font=h)
        self.mobile.grid(row=1, column=3, padx=20, pady=20)
        self.txt4 = Entry(self.formFrame1, width=30)
        self.txt4.grid(row=1, column=4, pady=20)
        self.txt4.insert(0, data[3])

        self.role = Label(self.formFrame1, text="Role", font=h)
        self.role.grid(row=2, column=1, padx=20, pady=20)
        self.txt5 = ttk.Combobox(self.formFrame1, values=('Super-Admin', 'Admin'))
        self.txt5.grid(row=2, column=2, pady=20)
        self.txt5.set(data[4])

        self.btn3=Button(self.root1,text="Update",width=15,font=('arial',12),command=self.update)
        self.btn3.pack()

    def update(self):
        n = self.txt1.get()
        e = self.txt2.get()
        idd=self.txt6.get()
        m = self.txt4.get()
        r = self.txt5.get()
        q=f"update admin set name='{n}',email='{e}',mobile='{m}',role='{r}' where id='{idd}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo('',"Information Updated")




if __name__ == '__main__':
    x=Main()