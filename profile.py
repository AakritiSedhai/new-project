from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Product")
window.geometry('640x420')
window.resizable(False,False)
window.config(bg="#0a3570")
product_img = ImageTk.PhotoImage(file="profile.png")

my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=product_img,anchor=NW)
my_canvas.pack(fill="both",expand=True)
home=ImageTk.PhotoImage((Image.open("home icon.png")))
home_btn=Button(window, image=home,bd=0,bg="#f2f2f2",activebackground="#f2f2f2")
home_btn.place(x=10, y=5)
change_user_btn1=Button(window,text="CHANGE USERNAME",font=("comic sans",12,"normal"),
                     bg="#ffbd59",width=18,fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
change_user_btn1.place(x=250,y=205)
change_PW_btn1=Button(window,text="CHANGE PASSWORD",font=("comic sans",12,"normal"),
                     bg="#ffbd59",width=18,fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
change_PW_btn1.place(x=250,y=287)
window.mainloop()