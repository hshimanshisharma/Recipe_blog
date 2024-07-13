from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import addcategory
import admin_change_password
import viewcategory
import view_user
import view_recipe2
import admin_rating_reviews
import addadmin
import viewadmin
import adduser
import add_recipe
import adminrecipe


class Main:
    def __init__(self,id,name,email,role):
        self.root = Tk()
        self.root.title('Admin Dashboard')
        self.root.state('zoomed')

        self.rootMenu = Menu(self.root) # Initializing Main Menu
        # Configuring root window to use rootMenu as its menu.
        self.root.configure(menu=self.rootMenu)

        '''
        # creating file menu
        self.fileMenu = Menu(self.rootMenu, tearoff=0)
        # Adding a button inside rootMenu and link it with fileMenu
        self.rootMenu.add_cascade(label="File", menu=self.fileMenu)
        # Adding Buttons inside fileMenu
        self.fileMenu.add_command(label="New Project")
        self.fileMenu.add_command(label="New...")
        self.fileMenu.add_command(label="New Scratch File")'''
        print(role)
        if role == "Super-admin":
            print("true")
            self.catMenu = Menu(self.rootMenu, tearoff=0)
            self.catMenu.add_command(label='Add Admin', command=lambda:addadmin.main())
            self.catMenu.add_command(label='View Admin', command=lambda :viewadmin.Main())
            self.rootMenu.add_cascade(label='Admin', menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add Category', command=lambda: addcategory.main())
        self.catMenu.add_command(label='View Category', command=lambda: viewcategory.main())
        self.rootMenu.add_cascade(label='Category', menu=self.catMenu)



        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.profileMenu.add_command(label='Add User', command=lambda: adduser.main())
        self.profileMenu.add_command(label='View User', command=lambda: view_user.Main())
        self.rootMenu.add_cascade(label='User', menu=self.profileMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        # self.profileMenu.add_command(label='Add Recipe', command=lambda: add_recipe.main())
        self.profileMenu.add_command(label='View Recipe ', command=lambda: view_recipe2.main())
        self.profileMenu.add_command(label='All Recipe Ratings ', command=lambda: admin_rating_reviews.main())
        self.rootMenu.add_cascade(label='Recipe', menu=self.profileMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.profileMenu.add_command(label='Recipes List', command=lambda: adminrecipe.Main())
        self.rootMenu.add_cascade(label='All Recipes', menu=self.profileMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.profileMenu.add_command(label='Change Password', command=lambda: admin_change_password.main(email))
        self.profileMenu.add_command(label='Logout', command=lambda: self.root.destroy())
        self.rootMenu.add_cascade(label='Profile', menu=self.profileMenu)

        self.lb = Label(self.root, text=f"Welcome {name}", font=('arial', 28, 'bold'))
        self.lb.pack(pady=20)

        self.root.mainloop()

    def openAddCategory(self):
        addcategory.main()

# obj = Main()