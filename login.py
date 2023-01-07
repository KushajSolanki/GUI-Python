from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Form")
window.geometry('350x350')

lbl1 = Label(window,text="Enter Username")
lbl2 = Label(window,text="Enter Password")
lbl1.grid(column=0,row=0)
lbl2.grid(column=0,row=1)

txt1 = Entry(window, width=20)
txt2 = Entry(window,width=20)
txt1.grid(column=1,row=0)
txt2.grid(column=1,row=1)

def login():
    user = txt1.get()
    pass1 = txt2.get()
    if(user==pass1):
        messagebox.showinfo('Login Window','Login Successfully')
    else:
        messagebox.showinfo('Login Window','Login Failed')

btn = Button(window,text="Login",bg="orange",fg="black",command=login)
btn.grid(column=2,row=0)

window.mainloop()