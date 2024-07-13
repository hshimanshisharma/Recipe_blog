import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect
import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('View')
        self.root.state('zoomed')

        self.mainlabel=tkinter.Label(self.root,text="VIEW CATEGORY",font=('arial',28,'bold'),foreground="#A80CB3")
        self.mainlabel.pack(pady=20)

        self.formframe=tkinter.Frame(self.root)
        self.formframe.pack()

        h = ('ariel', 15)
        self.lb1 = tkinter.Label(self.formframe, text="Search", font=('arail',15,'bold'),foreground="#48284A")
        self.lb1.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=30)
        self.txt.grid(row=0, column=1, padx=20)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 10), command=self.search,bg="#9E7AA1")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 10), command=self.getvalues,bg="#9E7AA1")
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=0, column=3, padx=20)

        self.table=ttk.Treeview(self.root,columns=('name','description'))
        self.table.pack(pady=20,expand=True,fill='both')
        self.table.heading('name',text="NAME")
        self.table.heading('description',text="DESCRIPTION")
        self.table['show']='headings'

        self.btn=tkinter.Button(self.root,text="DELETE",width=15,command=self.delete,bg="#9E7AA1")
        self.btn.pack(pady=10)

        self.table.bind("<Double-1>", self.open)

        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18), rowheight=40,foreground="white",background="#916C80")
        style.configure('Treeview.Heading', font=('arial', 23,'bold'), rowheight=40,foreground="#48284A")

        self.root.mainloop()

    def getvalues(self):
        conn=Conect()
        cr=conn.cursor()
        q="select * from category"
        cr.execute(q)
        data=cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c,value=i)
            c+=1

    def search(self):
        conn = Conect()
        cr = conn.cursor()
        s = self.txt.get()
        q = f"select * from category where name like '%{s}%'"
        cr.execute(q)
        data = cr.fetchall()

        for row in self.table.get_children():
            self.table.delete(row)
        c = 0
        for i in data:
            self.table.insert('', index=c, value=i)
            c += 1

    def delete(self):
        conn = Conect()
        cr = conn.cursor()
        rowid = self.table.selection()
        if len(rowid) == 0:
            msg.showinfo('', "Select a row!")
        elif len(rowid) > 1:
            msg.showinfo('', "Please select only one row at a time!!")
        else:
            items = self.table.item(rowid[0])
            data = items['values']
            q = f"delete from category where name='{data[0]}'"
            cr.execute(q)
            conn.commit()
            self.getvalues()
            msg.showinfo('', "Row Deleted")

    def open(self,e):
        data=self.table.item(self.table.selection()[0])['values']
        self.root1=Toplevel()
        self.root1.title('Update')
        self.root1.geometry('800x800')

        self.lb=tkinter.Label(self.root1,text="UPDATE CATEGORY",font=('arial',28))
        self.lb.pack(pady=20)

        self.formframe1 = Frame(self.root1)
        self.formframe1.pack()

        h = ('ariel', 15)
        self.name = Label(self.formframe1, text="Name", font=h)
        self.name.grid(row=0, column=1, pady=20, padx=20)
        self.txt1 = Entry(self.formframe1, width=30)
        self.txt1.grid(row=0, column=2, pady=20)
        self.txt1.insert(0,data[0])
        self.txt1.configure(state='readonly')

        self.descp = tkinter.Label(self.formframe1, text="Description", font=h)
        self.descp.grid(row=1, column=1, pady=20, padx=20)
        self.txt2 = tkinter.Entry(self.formframe1, width=30)
        self.txt2.grid(row=1, column=2, pady=20)
        self.txt2.insert(0,data[1])

        self.btn3 = tkinter.Button(self.root1, text="ADD", width=10, font=('arial', 15), command=self.add)
        self.btn3.pack(pady=20)

    def add(self):
        conn = Conect()
        cr = conn.cursor()
        n=self.txt1.get()
        d=self.txt2.get()
        q=f"update category set name='{n}', description='{d}'"
        cr.execute(q)
        conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo('',"Category Updated")

if __name__ == '__main__':
    x=main()