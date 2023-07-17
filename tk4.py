#Creating a button with colours and positioning them.
from tkinter import *
top=Tk()
#fg means foreground
#side is used to tell where to put the button
rb=Button(top,text="red",fg="red")
rb.pack(side=LEFT)
gb=Button(top,text="green",fg="green")
gb.pack(side=RIGHT)
bb=Button(top,text="blue",fg="blue")
bb.pack(side=TOP)
top.mainloop()