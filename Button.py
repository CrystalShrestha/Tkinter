from tkinter import *

root=Tk()

#Button without any function
myButton = Button(root, text = "Press")
myButton.pack()

#State disabled button
myButton1 = Button(root, text = "DONT!", state=DISABLED)
myButton1.pack()

#Button x and y padding

myButton2 = Button(root, text = "Click", padx=50)
myButton2.pack()

myButton3 = Button(root, text = "Big Click", padx=50, pady=50, bg="black", fg="red")
myButton3.pack()

root.mainloop()