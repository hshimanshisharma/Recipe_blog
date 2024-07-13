import tkinter
from tkinter import *
import tkinter.messagebox as msg

import Connection
from Connection import Conect
import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title('View User')
        self.root.state('zoomed')

        self.lb = tkinter.Label(self.root, text='VIEW RECIPES', font=('arial', 28,'bold'),foreground="#A80CB3")
        self.lb.pack(pady=20)

        self.formframe = tkinter.Frame(self.root)
        self.formframe.pack()

        h = ('arial', 15)
        self.lb1 = tkinter.Label(self.formframe, text="Search", font=('arail',15,'bold'),foreground="#48284A")
        self.lb1.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=30)
        self.txt.grid(row=0, column=1, padx=20)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 10), command=self.search,bg="#9E7AA1")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 10), command=self.getvalues,bg="#9E7AA1")
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=0, column=3, padx=20)

        self.table = ttk.Treeview(self.root, columns=('id', 'userid', 'recipeid', 'ratings', 'description'))
        self.table.pack(pady=10, expand=True, fill='both')
        self.btn = tkinter.Button(self.root, text="DELETE", width=15, command=self.delete,bg="#9E7AA1")
        self.btn.pack(pady=10)
        self.table.heading('id', text="ID")
        self.table.heading('userid', text="USER ID")
        self.table.heading('recipeid', text="RECIPE ID")
        self.table.heading('ratings', text="RATINGS")
        self.table.heading('description', text="REVIEW")
        self.table['show'] = 'headings'

        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18), rowheight=40,background="#916C80")
        style.configure('Treeview.Heading', font=('arial', 23,'bold'), rowheight=40,foreground="#48284A")

        self.root.mainloop()

    def getvalues(self):
        self.conn=Connection.Conect()
        self.cr=self.conn.cursor()
        q="select * from review"
        self.cr.execute(q)

        data=self.cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c , value=i)
            c+=1

    def search(self):
        self.conn=Connection.Conect()
        self.cr=self.conn.cursor()
        s=self.txt.get()
        q=f"select * from review where ratings like '%{s}%' or userid like '%{s}%' or recipe_id like '%{s}%' or id like '%{s}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()

        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c,value=i)
            c+=1

    def delete(self):
        rowid = self.table.selection()
        if len(rowid)==0:
            msg.showinfo('',"Select a row!")
        elif len(rowid)>1:
            msg.showinfo('',"Please select only one row at a time!!")
        else:
            items=self.table.item(rowid[0])
            data=items['values']
            q=f"delete from review where id='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo('',"Row Deleted",parent=self.root)

if __name__ == '__main__':
    x=main()