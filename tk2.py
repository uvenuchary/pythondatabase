#Creating a Button
from tkinter import *
a=Tk()
def hcall():
    print("Welcome")
A=Button(a,text="Hi",command=hcall)
A.pack()
a.mainloop()
