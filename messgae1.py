from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome")
window.geometry('200x200')

def hello():
    messagebox.showinfo('Login','Hello Python')
btn = Button(window,text='Click Here',command=hello)
btn.grid(column=0,row=0)
window.mainloop()
