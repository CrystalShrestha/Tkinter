from tkinter import *

top = Tk()
top.geometry("1280x720")


name = Label(top, text = "Name")
name.place(x = 620, y = 330)
password = Label(top, text = "Password ")
password.place(x = 620, y = 360)
contact = Label(top, text = "Contact ")
contact.place(x = 620, y = 390)
e1 = Entry(top).place(x = 680, y = 330)
e2 = Entry(top, show="*").place(x = 680, y = 360)
e3 = Entry(top).place(x = 680, y = 390)

submit = Button(top, text = "Submit").place(x = 710, y = 430)

top.mainloop()