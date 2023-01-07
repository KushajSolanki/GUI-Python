from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Length Window")
window.geometry('300x200')

lbl1 = Label(window,text="Enter Name")

lbl1.grid(column=0,row=0)
txt1 = Entry(window, width=30)
txt1.grid(column=1,row=0)

def login():
    user = txt1.get()
    length = len(user)
    if(length>0):
        messagebox.showinfo('Length Window',length)
    else:
        messagebox.showinfo('Login Of Name','Enter Name Again')

btn = Button(window,text="Enter",bg="orange",fg="black",command=login)
btn.grid(column=1,row=2)

window.mainloop()