from tkinter import *

root = Tk()

onebutton = Button(root, text = "START", bg = "black" , fg = "white")#creating a button widget
onebutton.pack(side = LEFT)#shoving it onto the screen

twobutton = Button(root, text = "STOP", bg = "red", fg = "white")
twobutton.pack(side = RIGHT)

threebutton = Button(root, text = "WHAT", fg = "green")
threebutton.pack(side = TOP)

fourbutton = Button(root, text = "HEH", fg = "blue")
fourbutton.pack(side = BOTTOM)

root.mainloop()
