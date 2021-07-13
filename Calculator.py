from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("400x900")
root.title("Calculator - Crystal")
root.wm_iconbitmap("D:\College\Calculator\calculator_3534.ico")
root.configure(bg='khaki3')


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=18, padx=50)

f = Frame(root, bg="khaki1")
b = Button(f, text="C", font="lucida 30 bold", padx=7, pady=8)
b.pack(side=LEFT, padx=8, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 30 bold", padx=17, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 30 bold", padx=7, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="khaki1")
b = Button(f, text="7", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="9", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="khaki1")
b = Button(f, text="4", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="6", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="khaki1")
b = Button(f, text="1", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 30 bold", padx=12, pady=8)
b.pack(side=LEFT, padx=9, pady=2)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="khaki1")
b = Button(f, text="0", font="lucida 30 bold", padx=60, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 30 bold", padx=10, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="khaki1")
b = Button(f, text="*", font="lucida 30 bold", padx=13, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 30 bold", padx=14, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 30 bold", padx=13, pady=8)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

f.pack()




root.mainloop()