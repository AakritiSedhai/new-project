from tkinter import *
from PIL import Image, ImageTk

#front end code
def deleteproductcall():
    window=Toplevel()
    window.title("Main Page")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    img1 = ImageTk.PhotoImage(file="delete product.png")
    my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
    my_canvas.create_image(0,0,image=img1,anchor=NW)
    my_canvas.pack(fill="both",expand=True)

    pn_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    pn_entry.place(x=260,y=162)
    sku_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    sku_entry.place(x=260,y=232)
    delete_btn1=Button(window,text="DELETE",font=("comic sans",12,"normal"),
                        bg="#ff1515",fg="#0c0c0c",border=0,activebackground="#ff1515",activeforeground="#0c0c0c")
    delete_btn1.place(x=283,y=316)

    window.mainloop()
