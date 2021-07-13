from tkinter import *

root = Tk()

e1 = Entry(root, width = 50, fg = "blue", bg = "white", borderwidth=5)
e1.pack()

def myClick():
    textoutput="Hey " + e1.get()

    myLabel = Button(root, text=textoutput)

    myLabel.pack()

myButton = Button(root, text="Press!", command=myClick)
myButton.pack()

root.mainloop()