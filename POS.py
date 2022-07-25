from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import datetime

def POScall():

    mydb=mysql.connector.connect(   #establishing connection with database
            host="localhost",
            user="root",
            password="",
            database="inventory")
    mycursor=mydb.cursor(buffered=True) #buffered=true will refresh the connection to database
    mycursor.execute("select * from product")
    fetch=mycursor.fetchall()

    def sell():
        sku=sku_entry.get()
        qnty=qnty_entry.get()
        if sku=="" or qnty=="": #to make all fields compulsory
            messagebox.showinfo("Alert","All fields are required")
        else:
            for row in fetch:
                if row[2]==sku: #to make sure the entered SKU exists
                    if int(row[1])>=int(qnty): #to restrict selling more than existing quantity
                        global aftersold
                        aftersold=int(row[1])-int(qnty) 
                        aftersold=str(aftersold) #holds the quantity after a product is sold
                        mycursor.execute("update product set Product_Quantity='"+aftersold+"' where Product_SKU='"+sku+"'")
                        messagebox.showinfo("Alert", "Product sold")
                        mydb.commit()
                        if int(row[1])<5:
                            messagebox.showinfo("Alert",row[0]+" is low on stock")
                        date=datetime.date.today() #to get today's date
                        newdate=date.strftime("%Y-%m-%d") #changing format of the date
                        
                        mycursor.execute("insert into transaction(Sold_Quantity,SKU,Transaction_Date) values('"+qnty+"','"+sku+"','"+newdate+"')")
                        mydb.commit()
                        break
                    else:
                        messagebox.showinfo("Alrert","You are trying to sell more than you have")
                        break
            else:
                messagebox.showinfo("Alert","No such prodcut exists")
            empty=""
            date="abc"
            # mycursor.execute("insert into transaction values('"+empty+"','"+aftersold+"','"+sku+"',"+date+")")
            
        
    
        
    window=Toplevel()
    window.title("Product")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")


    product_img = ImageTk.PhotoImage(file="POS.png")

    my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
    my_canvas.create_image(0,0,image=product_img,anchor=NW)
    my_canvas.pack(fill="both",expand=True)

    global sku_entry
    sku_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sku_entry.place(x=260,y=150)

    global qnty_entry
    qnty_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    qnty_entry.place(x=260,y=240)

    sell_product=Button(window,text="SELL PRODUCT",bd=0,font=("comic sans",14),bg="#ffbd59",width=15,
                fg="#0c0c0c",activeforeground="#0c0c0c",activebackground="#ffbd59",command=sell)
    sell_product.place(x=235,y=332)

    window.mainloop()







