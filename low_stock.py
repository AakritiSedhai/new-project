#Code to connect database to frontend
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
)
mycursor=mydb.cursor() 
mycursor.execute("select * from product where Product_Quantity<5") #Will fetch only products which have less than 5 quantity
fetch=mycursor.fetchall()

#Frontend code
from tkinter import *
from PIL import Image, ImageTk

def lowstockcall():
    window = Toplevel()
    window.title("Main Page")
    window.geometry('640x420+350+150')
    window.resizable(False, False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="low stock.png")
    my_canvas = Canvas(window, width=200, height=200, bg="#0a3570")
    my_canvas.create_image(0, 0, image=img1, anchor=NW)
    my_canvas.pack(fill="both", expand=True)

    entry1 = Entry(window,bd=1,state="normal", font=('Arial 12'),width=15,justify=CENTER)
    entry1.insert(0,"Product Name")
    entry1.place(x=30,y=90)

    entry2=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
    entry2.insert(0,"SKU")
    entry2.place(x=170,y=90)

    entry3=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
    entry3.insert(0,"Quantity")
    entry3.place(x=310,y=90)

    n=113

    for row in fetch: #Iterates through the number of rows that have been fetched

        entry1 = Entry(window,bd=1,state="normal", font=('Arial 12'),width=15,justify=CENTER)
        entry1.insert(1,row[0])
        entry1.place(x=30,y=n)

        entry2=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
        entry2.config(highlightbackground="red")
        entry2.insert(1,row[2])
        entry2.place(x=170,y=n)

        entry3=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
        entry3.insert(1,row[1])
        entry3.place(x=310,y=n)
        n=n+23

    window.mainloop()