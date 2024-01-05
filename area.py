import tkinter as tk

def perimeter():
    length = float(E1.get())
    width = float(E2.get())
    peri = 2 * length + 2 * width
    ans.config(text= peri)
def area():
    length = float(E1.get())
    width = float(E2.get())
    area = length * width
    ans.config(text= area)

root = tk.Tk()

l1 = tk.Label(root, text="enter length of the quadrilateral")
l1.pack()

E1 = tk.Entry(root)
E1.pack()

l2 = tk.Label(root, text="enter width of the quadrilateral")
l2.pack()

E2 = tk.Entry(root)
E2.pack()

B1 = tk.Button(root, text="calculate Perimeter", command = perimeter)
B1.pack()

B2 = tk.Button(root, text="calculate Area", command= area)
B2.pack()

ans = tk.Label(root, text="Answer will be displayed here")
ans.pack()

tk.mainloop()