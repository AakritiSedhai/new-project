#code to connect database to frontend

def signup(): 
    empty="" #for autoincrement field
    user=user_entry.get()
    pw=pw_entry.get()
    con_pw=con_pw_entry.get()
    if user=="" or pw=="" or con_pw=="": #to ensure all fields are entered
        messagebox.showinfo("Alert", "All fields are required")
    else:
        if pw_entry.get()==con_pw_entry.get(): #to ensure both passwords match
            import mysql.connector
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory")
            mycursor=mydb.cursor()
            mycursor.execute("select * from users")
            fetch=mycursor.fetchall() #fetching all the records
            for i in range(len(fetch)): #iterates through all the credentials
                new=list(fetch[i])
                if(new[1]==user): #checks if user already exists or not
                    messagebox.showinfo("Alert","User already exists")
                    break
            else:
                mycursor.execute("insert into users values('"+empty+"','"+user+"','"+pw+"')") #creating new record
                mycursor.execute("commit")
                mydb.close()
                window.destroy()
                
        else:
            messagebox.showinfo("Alert","Password and confirmed passsword don't match") #alert message if password doesnot match

    
#Frontend code
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox 
def signupcall():
    global window
    window=Toplevel() #to open another window on top
    window.title("Sign up")
    window.geometry('640x420+350+150')
    window.resizable(False,False)
    window.config(bg="#0a3570")
    signup_img = ImageTk.PhotoImage(file="signup.png")
    my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
    my_canvas.create_image(0,0,image=signup_img,anchor=NW)
    my_canvas.pack(fill="both",expand=True)
    
    global user_entry
    user_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    user_entry.place(x=320,y=100)
    global pw_entry
    pw_entry =Entry(window,show="*",bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    pw_entry.place(x=320,y=165)
    global con_pw_entry
    con_pw_entry =Entry(window,show="*",bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
    con_pw_entry.place(x=320,y=233)
    signup_btn1=Button(window,text="SIGN UP",font=("comic sans",14,"normal"),
                        bg="#ffbd59",width=12,fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c",command=signup)
    signup_btn1.place(x=269,y=304)

    window.mainloop()
