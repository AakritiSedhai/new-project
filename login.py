#codes to connect database and frontend

import mysql.connector #module to operate on database
from mainpage import *


def login():
    username=username_entry.get()
    password=password_entry.get()
    if username=="" or password=="":
        messagebox.showinfo("Alert","Both field are required")
    else:
        mydb=mysql.connector.connect(   #establishing connection with database
        host="localhost",
        user="root",
        password="",
        database="inventory")
        mycursor=mydb.cursor()
        mycursor.execute("select * from users")
        fetch=mycursor.fetchall() #fetching all the records
        for i in range(len(fetch)): #iterates through all the credentials
            new=list(fetch[i])
            if new[1]==username and new[2]==password:
                window.destroy() 
                mainpagecall() #link to mainpage
                break
        else:
            messagebox.showinfo("Alert","No such user")
                

#frontend code
from Signup import * #To link with signup window
def signupopen():
    signupcall()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
window=Tk()
window.title("Sign-in")
window.geometry('640x420+350+150')
window.resizable(False,False)
window.config(bg="#0a3570")

img1 = ImageTk.PhotoImage(file="loginimg.png")

my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=img1,anchor=NW)

my_canvas.pack(fill="both",expand=True)

signupopenB=Button(window,text="Dont have an account? Sign-up",fg="#d3b072",font=("comic sans",10),bg="#0a3570",bd=0,activeforeground="#d3b072",activebackground="#0a3570",command=signupopen)
signupopenB.place(x=380,y=320)

username_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
username_entry.place(x=433,y=103)

password_entry =Entry(window,show= "*", bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
password_entry.place(x=431,y=175)

log_in=Button(window,text="SIGN-IN",bd=0,font=("comic sans",17,"bold","underline"),bg="#ffbd59",width=11,
              fg="#0a3570",activeforeground="#0a3570",activebackground="#ffbd59", command= login)
log_in.place(x=390,y=240)

window.mainloop()
