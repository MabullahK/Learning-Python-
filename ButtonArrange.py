from tkinter import * 

root = Tk()
root.geometry("300x50")

F1 = Frame(root)
F1.pack(side = BOTTOM)

F2 = Frame(root)
F2.pack(side = TOP)

B1 = Button(F2,text ="+")
B1.pack(side = RIGHT)

B2 = Button(F2,text ="-")
B2.pack(side = RIGHT)

B3 = Button(F1,text ="X")
B3.pack(side = RIGHT)

B4 = Button(F1,text ="/")
B4.pack(side = RIGHT)

mainloop()