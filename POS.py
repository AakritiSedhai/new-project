from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
window=Tk()
window.title("Product")
window.geometry('640x420')
window.resizable(False,False)
window.config(bg="#0a3570")


product_img = ImageTk.PhotoImage(file="POS.png")

my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=product_img,anchor=NW)
my_canvas.pack(fill="both",expand=True)

sku_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
sku_entry.place(x=260,y=150)

qnty_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
qnty_entry.place(x=260,y=240)

sell_product=Button(window,text="SELL PRODUCT",bd=0,font=("comic sans",14),bg="#ffbd59",width=15,
              fg="#0c0c0c",activeforeground="#0c0c0c",activebackground="#ffbd59")
sell_product.place(x=235,y=332)



window.mainloop()







