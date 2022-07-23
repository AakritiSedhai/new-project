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
home=ImageTk.PhotoImage((Image.open("home icon.png")))
home_btn=Button(window, image=home,bd=0,bg="#f2f2f2",activebackground="#f2f2f2")
home_btn.place(x=10, y=5)
# scroll = Scrollbar(window)
# scroll.pack(side=RIGHT, fill=Y)

# scroll = Scrollbar(window,orient='horizontal')
# scroll.pack(side= BOTTOM,fill=X)

# POS = ttk.Treeview(window,yscrollcommand=scroll.set)
# POS.pack()
# scroll.config(command=POS.yview)
# POS['columns'] = ('PRODUCT NAME', 'QUANTITY', 'SKU',"PRICE","QUANTITY","SELECT")
# # format our column
# POS.column("#0", width=0,  stretch=NO)
# POS.column("PRODUCT NAME",anchor=CENTER, width=40)
# POS.column("QUANTITY",anchor=CENTER,width=40)
# POS.column("SKU",anchor=CENTER,width=40)
# POS.column("PRICE",anchor=CENTER,width=40)
# POS.column("QUANTITY",anchor=CENTER,width=40)
# POS.column("SELECT",anchor=CENTER,width=40)
#
# #Create Headings
# POS.heading("#0",text="",anchor=CENTER)
# POS.heading("PRODUCT",text="product",anchor=CENTER)
# POS.heading("QUANTITY",text="quantity",anchor=CENTER)
# POS.heading("SKU",text="sku",anchor=CENTER)
# POS.heading("PRICE",text="price",anchor=CENTER)
# POS.heading("QUANTITY",text="quantity",anchor=CENTER)
# POS.heading("SELECT",text="select",anchor=CENTER)
# #labels
# product= Label(window,text = "PRODUCT",fg="#ffffff",bg="#0a3570")
# product.grid(row=0,column=0 )
#
# QUANTITY1 = Label(window,text="QUANTITY",fg="#ffffff",bg="#0a3570")
# QUANTITY1.grid(row=0,column=1)
#
# sku= Label(window,text="SKU",fg="#ffffff",bg="#0a3570")
# sku.grid(row=0,column=2)
# PRICE= Label(window,text="PRICE",fg="#ffffff",bg="#0a3570")
# PRICE.grid(row=0,column=3)
# QUANTITY2= Label(window,text="QUANTITY",fg="#ffffff",bg="#0a3570")
# QUANTITY2.grid(row=0,column=4)
# SELECT= Label(window,text="SELECT",fg="#ffffff",bg="#0a3570")
# SELECT.grid(row=0,column=5)
#
# #Entry boxes
# product_entry= Entry(window)
# product_entry.grid(row= 1, column=0)
#
# QUANTITY1_entry = Entry(window)
# QUANTITY1_entry.grid(row=1,column=1)
#
# sku_entry = Entry(window)
# sku_entry.grid(row=1,column=2)
#
# PRICE_entry = Entry(window)
# PRICE_entry.grid(row=1,column=3)
#
# QUANTITY2_entry = Entry(window)
# QUANTITY2_entry.grid(row=1,column=4)
#
# SELECT_entry = Entry(window)
# SELECT_entry.grid(row=1,column=5)

# class Table:
#     # Initialize a constructor
#     def __init__(self, window):
#
#         # An approach for creating the table
#         for i in range(total_rows):
#             for j in range(total_columns):
#                 print(i)
#                 if i ==0:
#                     self.entry = Entry(window, width=20, bg='LightSteelBlue',fg='Black',
#                                        font=('Arial', 16, 'bold'))
#                 else:
#                     self.entry = Entry(window, width=20, fg='blue',
#                                font=('Arial', 16, ''))
#
#                 self.entry.grid(row=i, column=j)
#                 self.entry.insert(END, employee_list[i][j])
# employee_list = [('ID', 'Name', 'City', 'Age'),
#         (1, 'Gorge', 'California', 30),
#        (2, 'Maria', 'New York', 19),
#        (3, 'Albert', 'Berlin', 22),
#        (4, 'Harry', 'Chicago', 19),
#        (5, 'Vanessa', 'Boston', 31),
#        (6, 'Ali', 'Karachi', 30)]
#
# total_rows = len(employee_list)
# total_columns = len(employee_list[0])

lf = LabelFrame(my_canvas,background="#ffffff")

# Add a label in the labelFrame widget
label= Label(lf, text= "PRODUCT")
label.config(font= 'Arial 9',bg="#0a3570",fg="#ffffff")
label.place(x=50,y=55)

lf.pack()


window.mainloop()







