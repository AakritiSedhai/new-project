from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

#connecting frontend to database
def update():
    mydb=mysql.connector.connect(   #establishing connection with database
        host="localhost",
        user="root",
        password="",
        database="inventory")
    mycursor=mydb.cursor()
    sku=sku1_entry.get()
    try: #disallow entering strings in quantity
        qnty=int(qnty1_entry.get())
    except:
        messagebox.showinfo("alert","cannot be string")
    else:
        qnty=str(qnty)
        mycursor.execute("select * from product") 
        records=mycursor.fetchall()
        if qnty=="": #to not allow null entries
            messagebox.showinfo("Alert","Quantity cannot be null")
        else:
            for row in records:
                if row[2]==sku: #to check if the product with gives sku exists or not
                    mycursor.execute("update product set Product_Quantity='"+qnty+"' where Product_SKU='"+sku+"'")
                    mydb.commit()
                    messagebox.showinfo("Alert","Quantity updated successfully")
                    break
            else:
                messagebox.showinfo("Alert","No such product found")

#front end code
def editproductcall():
    window=Toplevel()
    window.title("Main Page")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="Edit Product.png")
    my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
    my_canvas.create_image(0,0,image=img1,anchor=NW)
    my_canvas.pack(fill="both",expand=True)
    
    global sku1_entry
    sku1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sku1_entry.place(x=260,y=150)

    global qnty1_entry
    qnty1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    qnty1_entry.place(x=260,y=240)
    
    edit_btn1=Button(window,text="UPDATE QUANTITY",font=("comic sans",12,"normal"),
                        bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=update)
    edit_btn1.place(x=245,y=293)
    window.mainloop()