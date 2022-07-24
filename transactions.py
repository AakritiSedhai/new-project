from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Main Page")
window.geometry('640x420+350+150')
window.resizable(False, False)
window.config(bg="#0a3570")

img1 = ImageTk.PhotoImage(file="transactions.png")
my_canvas = Canvas(window, width=200, height=200, bg="#0a3570")
my_canvas.create_image(0, 0, image=img1, anchor=NW)
my_canvas.pack(fill="both", expand=True)
window.mainloop()