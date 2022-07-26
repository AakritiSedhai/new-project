from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

def transactionscall():

    #connecting frontend to database
    mydb=mysql.connector.connect( #connecting to database
        host="localhost",
        user="root",
        password="",
        database="inventory"
    )

    #frontend code
    window = Toplevel()
    window.title("Transactions")
    window.geometry('640x420+350+150')
    window.resizable(False, False)
    window.config(bg="#0a3570")

    img1 = ImageTk.PhotoImage(file="transactions.png")
    my_canvas = Canvas(window, width=200, height=200, bg="#0a3570")
    my_canvas.create_image(0, 0, image=img1, anchor=NW)
    my_canvas.pack(fill="both", expand=True)

    entry1 = Entry(window,bd=1,state="normal", font=('Arial 12'),width=15,justify=CENTER)
    entry1.insert(0,"Product Name")
    entry1.place(x=50,y=90)

    entry2=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
    entry2.insert(0,"Sold Quantity")
    entry2.place(x=190,y=90)

    entry3=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
    entry3.insert(0,"SKU")
    entry3.place(x=330,y=90)

    entry4=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
    entry4.insert(0,"Transaction Date")
    entry4.place(x=470,y=90)

    mycursor=mydb.cursor()
    mycursor.execute("select * from transaction") 
    fetch=mycursor.fetchall()
    n=112

    for row in fetch: #to iterate through the number of transaction row
        sku=row[2]
        tdate=row[3]
        sold=row[1]
        mycursor.execute("select * from product where Product_SKU='"+sku+"'") #using SKU has the foreign key
        fetch2=mycursor.fetchall()
        productn=(fetch2[0])[0] #to get the corresponding product which was sold
        entry1 = Entry(window,bd=1,state="normal", font=('Arial 12'),width=15,justify=CENTER)
        entry1.insert(0,productn)
        entry1.place(x=50,y=n)

        entry2=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
        entry2.insert(0,sold)
        entry2.place(x=190,y=n)

        entry3=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
        entry3.insert(0,sku)
        entry3.place(x=330,y=n)

        entry4=Entry(window,bd=1, font=('Arial 12'),width=15,justify=CENTER)
        entry4.insert(0,tdate)
        entry4.place(x=470,y=n)
        n=n+22
            
    window.mainloop()