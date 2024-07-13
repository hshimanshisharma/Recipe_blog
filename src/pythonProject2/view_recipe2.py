import tkinter
from tkinter import *
import tkinter.messagebox as msg
from Connection import Conect
import tkinter.ttk as ttk
from gtts import gTTS
import playsound
import os
import threading

class main:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('View')
        self.root.state('zoomed')

        self.mainlabel = tkinter.Label(self.root, text="VIEW RECIPES", font=('arial', 28,'bold'),foreground="#A80CB3")
        self.mainlabel.pack(pady=20)

        self.formframe = tkinter.Frame(self.root)
        self.formframe.pack()
        h = ('ariel', 15)

        self.lb1 = tkinter.Label(self.formframe, text="Search", font=('arial', 15,'bold'),foreground="#48284A")
        self.lb1.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=30)
        self.txt.grid(row=0, column=1, padx=20)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 10), command=self.search,bg="#9E7AA1")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 10), command=self.getvalues,bg="#9E7AA1")
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=0, column=3, padx=20)

        self.table = ttk.Treeview(self.root, columns=('id','name', 'description','duration','ingredients','category'))
        self.table.pack(pady=20,padx=20, expand=True, fill='both')
        self.table.heading('id', text="ID")
        self.table.heading('name', text="NAME")
        self.table.heading('description', text="DESCRIPTION")
        self.table.heading('duration', text="DURATION")
        self.table.heading('ingredients', text="INGREDIENTS")
        self.table.heading('category', text="CATEGORY")
        self.table['show'] = 'headings'

        self.table.column('id',width=5, anchor=CENTER)
        # self.table.column('name', width=20)
        # self.table.column('description', width=20)
        self.table.column('duration', width=5, anchor=CENTER)
        self.table.column('ingredients', width=20)
        self.table.column('category', width=20,anchor=CENTER)

        self.btn = tkinter.Button(self.root, text="DELETE", width=15, command=self.delete,bg="#9E7AA1")
        self.btn.pack(pady=10)

        self.table.bind("<Double-1>", self.open)

        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18), rowheight=25,foreground="white",background="#916C80")
        style.configure('Treeview.Heading', font=('arial', 23,'bold'), rowheight=40,foreground="#48284A")

        self.root.mainloop()

    def getvalues(self):
        conn = Conect()
        cr = conn.cursor()

        q = f"select * from recipe"
        print(q)
        cr.execute(q)
        data = cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c = 0
        for i in data:
            self.table.insert('', index=c, value=i)
            c += 1

    def search(self):
        conn = Conect()
        cr = conn.cursor()
        s = self.txt.get()
        q = f"select * from recipe where name like '%{s}%' or duration like '%{s}%' or ingredients like'%{s}%' or category like '%{s}%'"
        cr.execute(q)
        data = cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c,value=i)
            c+=1

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
            print (data)
            q = f"delete from recipe where id='{data[0]}'"
            cr.execute(q)
            conn.commit()
            os.remove(f"recipy_images/{data[0]}.png")
            self.getvalues()
            msg.showinfo('', "Row Deleted")

    def open(self,e):
        data=self.table.item(self.table.selection()[0])['values']
        self.root1=Toplevel()
        self.root1.title('Update')
        self.root1.geometry('800x800')

        self.lb=tkinter.Label(self.root1,text="UPDATE RECIPE",font=('arial',28))
        self.lb.pack(pady=20)

        self.formframe1 = Frame(self.root1)
        self.formframe1.pack()

        h = ('arial', 15)

        self.id = Label(self.formframe1, text="ID", font=h)
        self.id.grid(row=0, column=1, padx=20, pady=20)
        self.tx = Entry(self.formframe1, width=30)
        self.tx.grid(row=0, column=2, pady=20)
        self.tx.insert(0, data[0])
        self.tx.configure(state='readonly')

        self.name = Label(self.formframe1, text="Name", font=h)
        self.name.grid(row=1, column=1, pady=20, padx=20)
        self.txt1 = Entry(self.formframe1, width=30)
        self.txt1.grid(row=1, column=2, pady=20)
        self.txt1.insert(0,data[1])
        # self.txt1.configure(state='readonly')

        self.descp = tkinter.Label(self.formframe1, text="Description", font=h)
        self.descp.grid(row=2, column=1, pady=20, padx=20)
        self.txt2 = tkinter.Text(self.formframe1, width=30,height=10)
        self.txt2.grid(row=2, column=2, pady=20)
        self.txt2.insert('1.0',data[2])

        self.dur = tkinter.Label(self.formframe1, text="Duration", font=h)
        self.dur.grid(row=3, column=1, pady=20, padx=20)
        self.tx1 = tkinter.Entry(self.formframe1, width=30)
        self.tx1.grid(row=3, column=2, pady=20)
        self.tx1.insert(0, data[3])

        self.ing = tkinter.Label(self.formframe1, text="Ingredients", font=h)
        self.ing.grid(row=4, column=1, pady=20, padx=20)
        self.tx2 = tkinter.Entry(self.formframe1, width=30)
        self.tx2.grid(row=4, column=2, pady=20)
        self.tx2.insert(0, data[4])

        self.cat = tkinter.Label(self.formframe1, text="Category", font=h)
        self.cat.grid(row=5, column=1, pady=20, padx=20)
        self.tx3 = ttk.Combobox(self.formframe1, state='readonly', values=self.getcat())
        self.tx3.grid(row=5, column=2, pady=20)
        self.tx3.set(data[5])


        self.btn3 = tkinter.Button(self.root1, text="Submit", width=10, font=('arial', 15), command=self.update)
        self.btn3.pack(pady=20)

        self.btn4 = tkinter.Button(self.root1, text="PLAY", width=10, font=('arial', 15), command=lambda: threading.Thread(target=self.play).start())

        self.btn4.pack(pady=20)

    def getcat(self):
        conn = Conect()
        cr = conn.cursor()
        q = "select name from category"
        cr.execute(q)
        result = cr.fetchall()
        lst=[]
        for i in result:
            lst.append(i[0])
        print (lst)
        return lst

    def play(self):
        lst= os.listdir('.')
        print(lst)
        if 'hello.mp3' in lst:
            os.remove('hello.mp3')
        text1= self.txt2.get('1.0','end-1c')
        obj = gTTS(text=text1,lang='en')
        obj.save("hello.mp3")
        playsound.playsound('hello.mp3')
        os.remove('hello.mp3')


    def update(self):
        conn = Conect()
        cr = conn.cursor()
        n = self.txt1.get()
        des = self.txt2.get('1.0','end-1c')
        dur=self.tx1.get()
        ing = self.tx2.get()
        cat = self.tx3.get()
        idd=self.tx.get()
        q=f"update recipe set name='{n}',description='{des}',ingredients='{ing}',duration='{dur}',category='{cat}' where id='{idd}'"
        cr.execute(q)
        conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo('',"Information Updated")

if __name__ == '__main__':
    x=main()