from tkinter import *

home = Tk()

frame = Frame(home)
frame.pack()

bottemframe = Frame(home)
bottemframe.pack(side=BOTTOM)

BlueButton = Button(frame,text="I am blue", fg = "blue")
BlueButton.pack(side=LEFT)

notBlueButton = Button(frame,text="I am not blue", fg = "purple")
notBlueButton.pack(side=LEFT)

notNotBlueButton = Button(frame,text="I am not, not blue", fg = "red")
notNotBlueButton.pack(side=RIGHT)

home.mainloop()
