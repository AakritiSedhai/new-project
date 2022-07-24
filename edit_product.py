from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Main Page")
window.geometry('640x420')
window.resizable(False,False)
window.config(bg="#0a3570")
img1 = ImageTk.PhotoImage(file="edit product.png")
my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
my_canvas.create_image(0,0,image=img1,anchor=NW)
my_canvas.pack(fill="both",expand=True)

pn1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
pn1_entry.place(x=260,y=108)
sku1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
sku1_entry.place(x=260,y=180)
qnty1_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
qnty1_entry.place(x=260,y=270)
edit_btn1=Button(window,text="UPDATE QUANTITY",font=("comic sans",12,"normal"),
                     bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
edit_btn1.place(x=245,y=330)
window.mainloop()