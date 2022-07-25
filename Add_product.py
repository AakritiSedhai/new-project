from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
#connecting database to backend
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="inventory",
    )
mycursor=mydb.cursor()
mycursor.execute("select * from product")
fetch=mycursor.fetchall()

def addproduct(): #function to add products
    pn=pn2_entry.get()
    qty=qnty_entry.get()
    sku=sku1_entry.get()
    sp=sp_entry.get()
    if pn=="" or qty=="" or sku=="" or sp=="": #avoids fields from being null
        messagebox.showinfo("Alert","All fields are required")
    else:
        for row in fetch:
            if row[2]==sku: #ensures that skus are not duplicated
                messagebox.showinfo("Alert","Product with same SKU already exists")
                break
        else:
            mycursor.execute("insert into product values('"+pn+"',"+qty+",'"+sku+"',"+sp+")")
            messagebox.showinfo("Alert","Product added successfully")
            mydb.commit()

#front end code
def addproductcall():
    window=Toplevel()
    window.title("Add product")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="add product.png")
    my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
    my_canvas.create_image(0,0,image=img1,anchor=NW)
    my_canvas.pack(fill="both",expand=True)
    global pn2_entry
    pn2_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    pn2_entry.place(x=57,y=133)
    global sku1_entry
    sku1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sku1_entry.place(x=269,y=223)
    global qnty_entry
    qnty_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    qnty_entry.place(x=269,y=131)
    global sp_entry
    sp_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sp_entry.place(x=57,y=223)
    add_btn1=Button(window,text="ADD  ",font=("comic sans",12,"normal"),
                        bg="#ffbd59",width=8,fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=addproduct)
    add_btn1.place(x=75,y=298)
    window.mainloop()
