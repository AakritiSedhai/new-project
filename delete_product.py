from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

def deleteproductcall():

    #connecting to database
    
    mydb=mysql.connector.connect(   #establishing connection with database
        host="localhost",
        user="root",
        password="",
        database="inventory")
    mycursor=mydb.cursor()
    mycursor.execute("select * from product")
    records=mycursor.fetchall()

    def deleteproduct(): #dunction to delete product
        pn=pn_entry.get()
        sku=sku_entry.get()
        for row in records: #iterates through all records in inventory
            if row[0]==pn and row[2]==sku: #makes sure the deleted product already exists
                mycursor.execute("delete from product where Product_Name='"+pn+"' and Product_SKU='"+sku+"'")
                messagebox.showinfo('Alert',"Product deleted successfully")
                mydb.commit()
                break
        else: 
            messagebox.showinfo('Alert',"No such product exists")
                

    #front end code

    window=Toplevel()
    window.title("Delete Product")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="delete product.png")
    my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
    my_canvas.create_image(0,0,image=img1,anchor=NW)
    my_canvas.pack(fill="both",expand=True)

    global pn_entry
    pn_entry=Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    pn_entry.place(x=260,y=162)
    
    global sku_entry
    sku_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sku_entry.place(x=260,y=232)
    delete_btn1=Button(window,text="DELETE",font=("comic sans",12,"normal"),
                        bg="#ff1515",fg="#0c0c0c",border=0,activebackground="#ff1515",activeforeground="#0c0c0c",command=deleteproduct)
    delete_btn1.place(x=283,y=316)

    window.mainloop()
