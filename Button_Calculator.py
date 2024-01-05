from tkinter import *


def add():
    N1 = float(E1.get())
    N2 = float(E2.get())
    A = N1 + N2
    Ans.config(text = f"{N1} + {N2} = {A}")

def subtract():
    N1 = float(E1.get())
    N2 = float(E2.get())
    A = N1 - N2
    Ans.config(text = f"{N1} - {N2} = {A}")

def multiply():
    N1 = float(E1.get())
    N2 = float(E2.get())
    A = N1 * N2
    Ans.config(text = f"{N1} X {N2} = {A}")

def divide():
    N1 = float(E1.get())
    N2 = float(E2.get())
    A = N1 / N2
    Ans.config(text =f"{N1} / {N2} = {A}")

root = Tk()

root.geometry("500x200")

root.title("Calculator")



l1 = Label(root, text="Enter First Number:")
l1.pack()

E1 = Entry(root)
E1.pack()

l2 = Label(root, text="Enter Second Number:")
l2.pack()

E2 = Entry(root)
E2.pack()

F1 = Frame(root)
F1.pack()

B1 = Button(F1, text="+", command = add)
B1.pack(side = RIGHT)

B2 = Button(F1, text="-",command = subtract)
B2.pack(side = RIGHT)

B3 = Button(F1, text="x", command = multiply)
B3.pack(side = RIGHT)

B4 = Button(F1, text="/", command = divide)
B4.pack(side = RIGHT)


Ans = Label(root, text="Answer will be displayed here")
Ans.pack()


mainloop()
