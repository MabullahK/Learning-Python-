import tkinter as tk

home = tk.Tk()

Click_me = tk.Button(home, text = "click me",command = home.destroy).pack()

home.title("Title")

L1 = tk.Label(home,text = "description").pack()

E1 = tk.Entry(home).pack()

home.mainloop()
