import pymysql
# import tkinter.messagebox as msg
def Conect():
    c=pymysql.connect(host='localhost', user='root', password='system', database='python_project')
    return c

def verifyEmail(mail):
    if "@" in mail and "." in mail:
        return "Valid"
    else:
        return "Invalid"

def verifyMobile(mobile):
    if len(mobile)==10:
        if mobile[0] in "6789":
            return "Valid"
        else:
            return "Invalid"



# conn=Conect()
# cr= conn.cursor()
# name=input("enter name")
# email=input("enter email")
# password=input("enter password")
# mobile=input("enter mobile")
# role=input("enter role")
# q=f"insert into admin values(null,'{name}' , '{email}', '{mobile}','{password}','{role}')"
# cr.execute(q)
# conn.commit()

