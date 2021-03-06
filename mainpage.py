from tkinter import *
from PIL import Image, ImageTk
from Dashboard import *
from product_page import *
from low_stock import *
from transactions import *
from POS import *

def mainpagecall():

    def dashboardopen(): #linking to dashboard page
        dashboardcall()
        
    def productpageopen(): #linking to product page
        productpagecall()

    def lowstockopen(): #linking to lowstock page
        lowstockcall()

    def transactionsopen(): #linking to lowstock page
        transactionscall()

    def POSopen(): #linking to POS page
        POScall()


    window=Tk()
    window.title("Main Page")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    
    img1 = ImageTk.PhotoImage(file="page2.png")
    my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
    my_canvas.create_image(0,0,image=img1,anchor=NW)
    my_canvas.pack(fill="both",expand=True)
    
    dashboard_btn=Button(window,text="DASHBOARD",font=("comic sans",18,"normal"),
                        bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=dashboardopen)
    dashboard_btn.place(x=109,y=97)
    
    product_btn=Button(window,text="PRODUCT",font=("comic sans",18,"normal"),
                    bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=productpageopen)
    product_btn.place(x=423,y=97)

    low_stock_btn=Button(window,text="LOW STOCK",font=("comic sans",18,"normal"),
                        bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=lowstockopen)
    low_stock_btn.place(x=111,y=205)

    transactions_btn=Button(window,text="TRANSACTION",font=("comic sans",18,"normal"),
                            bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=transactionsopen)
    transactions_btn.place(x=405,y=205)

    pos_btn=Button(window,text="POINT OF SALES",font=("comic sans",18,"normal"),
                            bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=POSopen)
    pos_btn.place(x=245,y=313)


    window.mainloop()
