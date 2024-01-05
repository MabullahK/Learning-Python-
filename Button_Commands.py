import tkinter as tk

Home = tk.Tk()

def changeColour():
    by.configure(bg="white", fg="white")
    L.configure(bg="white", fg="white")

def changeText():
    rw.configure(text="You pressed me")



gb = tk.Button(Home,text="Press me", bg="green", fg="blue",command=Home.destroy)
gb.pack()

by = tk.Button(Home,text="Press me", bg="black", fg="yellow", command=changeColour)
by.pack()

rw = tk.Button(Home,text="Press me", bg="red", fg="white", command=changeText)
rw.pack()

L = tk.Label(Home,text="Type anything...", bg="grey", fg="black")
L.pack()

Home.mainloop()
