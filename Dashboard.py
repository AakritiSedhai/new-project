
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
def dashboardcall():
    #Connecting front end and database
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from product")
    fetch=mycursor.fetchall()

    #front end code
    window = Toplevel()
    window.title("Dashboard")
    window.geometry('640x420+350+150')
    window.resizable(False, False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="Dashboard.png")
    my_canvas = Canvas(window, width=200, height=200, bg="#0a3570")
    my_canvas.create_image(0, 0, image=img1, anchor=NW)
    my_canvas.pack(fill="both", expand=True)
    n=120

    entry1 = Entry(window,bd=1,state="normal", font=('Arial 16'),width=15)
    entry1.insert(0,"Product Name")
    entry1.place(x=30,y=90)

    entry2=Entry(window,bd=1, font=('Arial 16'),width=15)
    entry2.insert(0,"SKU")
    entry2.place(x=215,y=90)

    entry3=Entry(window,bd=1, font=('Arial 16'),width=15)
    entry3.insert(0,"Quantity")
    entry3.place(x=400,y=90)


    for row in fetch:

        entry1 = Entry(window,bd=1,state="normal", font=('Arial 16'),width=15)
        entry1.insert(1,row[0])
        entry1.place(x=30,y=n)

        entry2=Entry(window,bd=1, font=('Arial 16'),width=15)
        entry2.config(highlightbackground="red")
        entry2.insert(1,row[2])
        entry2.place(x=215,y=n)

        entry3=Entry(window,bd=1, font=('Arial 16'),width=15)
        entry3.insert(1,row[1])
        entry3.place(x=400,y=n)
        n=n+30



    window.mainloop()