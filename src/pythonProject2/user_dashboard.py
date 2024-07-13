import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import adduser
import change_password
import add_recipe
import view_recipe
import view_user
import recipy_view
import user_rating_review

class main:
    def __init__(self,id,email,name):
        self.root=Tk()
        self.root.title('Dashboard')
        self.root.state('zoomed')
        self.root.configure(bg="#DAB6FC")

        self.rootmenu = Menu(self.root)
        self.root.configure(menu=self.rootmenu)

        self.user=Menu(self.rootmenu,tearoff=0)
        self.user.add_command(label='Add User',command=lambda :adduser.main())
        self.user.add_command(label='View User', command=lambda: view_user.Main())
        self.rootmenu.add_cascade(label='User', menu=self.user)

        self.profileMenu = Menu(self.rootmenu, tearoff=0)
        self.profileMenu.add_command(label='Add Recipe', command=lambda: add_recipe.main(id))
        self.profileMenu.add_command(label='View Recipe' , command=lambda : view_recipe.main(id))
        self.profileMenu.add_command(label='View Recipe Details', command=lambda: recipy_view.Main(id,name))
        self.profileMenu.add_command(label='View Recipe Ratings', command=lambda: user_rating_review.main(id))
        self.rootmenu.add_cascade(label='Recipe', menu=self.profileMenu)

        self.profileMenu = Menu(self.rootmenu, tearoff=0)
        self.profileMenu.add_command(label='Change Password', command=lambda: change_password.main(email))
        self.profileMenu.add_command(label='Logout', command=lambda: self.root.destroy())
        self.rootmenu.add_cascade(label='Profile', menu=self.profileMenu)

        self.lb = tkinter.Label(self.root, text=f"Welcome {name}",font=('arial',28,'bold'),bg="#DAB6FC")
        self.lb.pack(pady=20)

        self.root.mainloop()

if __name__ == '__main__':
    x=main(1,"mehak@gmail.com","Mehak")