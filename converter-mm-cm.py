import tkinter as tk

def cm2mm():
    try:
        cm = float(E1.get())
        ans = cm * 10
        Ans.config(text=f"{cm} cm = {ans} mm")

    except:
        Ans.config(text="invalid input")
def mm2cm():
    try:
        mm = float(E2.get())
        ans = mm / 10
        Ans.config(text=f"{mm} mm = {ans} cm")

    except:
        Ans.config(text="invalid input")
        
root = tk.Tk()

l1 = tk.Label(root, text="enter cm")
l1.pack()

E1 = tk.Entry(root)
E1.pack()

l2 = tk.Label(root, text="enter mm")
l2.pack()

E2 = tk.Entry(root)
E2.pack()

B1 = tk.Button(root, text="cm - mm", command= cm2mm)
B1.pack()

B2 = tk.Button(root, text="mm - cm", command= mm2cm)
B2.pack()

Ans = tk.Label(root, text="Answer will be displayed here")
Ans.pack()

tk.mainloop()