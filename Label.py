from tkinter import *

root = Tk()

#creating a label widget
Le1 = Label(root, text = "Tanananananan")
Le2 = Label(root, text = "Rararararararar")
Le3 = Label(root, text = "Tururururururur")
Le4 = Label(root, text = "Dududududududu")
Le5 = Label(root, text = "Shurururururur")


#shoving it in the screen - grid
Le1.grid(row = 0, column = 0)
Le2.grid(row = 3, column = 5)
Le3.grid(row = 2, column = 10)
Le4.grid(row = 1, column = 5)
Le5.grid(row = 5, column = 0)


root.mainloop()

