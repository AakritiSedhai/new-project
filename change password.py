from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Product")
window.geometry('640x420')
window.resizable(False,False)
window.config(bg="#0a3570")
product_img = ImageTk.PhotoImage(file="change password.png")

my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=product_img,anchor=NW)
my_canvas.pack(fill="both",expand=True)

update_pw_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
update_pw_entry.place(x=340,y=130)
confirm_pw_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
confirm_pw_entry.place(x=340,y=187)
update_pw_btn1=Button(window,text="UPDATE PASSWORD",font=("comic sans",14,"normal"),
                     bg="#ffbd59",width=18,fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
update_pw_btn1.place(x=230,y=261)
window.mainloop()