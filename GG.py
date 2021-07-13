
from tkinter import *
from tkinter.ttk import *


root = Tk()


Label(root, text='Calculator', font=('Verdana', 15)).pack(side=TOP, pady=10)


photo = PhotoImage(file=r"D:\College\Calculator\pngtree-cartoon-grey-calculator-illustration-png-image_4714635.jpg")


Button(root, text='Click Me !', image=photo).pack(side=TOP)

root.mainloop()