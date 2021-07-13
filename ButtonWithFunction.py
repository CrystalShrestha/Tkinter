from tkinter import *

root = Tk()

def function():
    Le1 = Label(root, text="Why?? \n Why Why Why?")
    Le1.grid(row = 5, column = 5)

Butt = Button(root, text="Don't Please!", command = function, fg = "red", bg="white")
Butt.grid(row = 4, column = 5)

root.mainloop()