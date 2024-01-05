import tkinter as tk

def Calculate():
    try:
        Num1 = float(N1.get())

        Num2 = float(N2.get())

        operator = option.get()

        if operator == "+":
            ans.set(Num1 + Num2)
            
        elif operator == "-":
            ans.set(Num1 - Num2)

        elif operator == "*":
            ans.set(Num1 * Num2)

        elif operator == "/":
            if N2 != 0:
                ans.set(Num1 / Num2 )
            else:
                ans.set("Error: Division by 0")
    except ValueError:
        ans.set("Invalid input")



home = tk.Tk()

home.title("Calculator")

l1=tk.Label(home,text="Enter a number")
l1.pack()

N1 = tk.Entry(home)
N1.pack()

option = tk.StringVar(home)
option.set("+")
DD = tk.OptionMenu(home,option,"+","-","/","*")
DD.pack()

l2 = tk.Label(home,text="Enter a number")
l2.pack()

N2 = tk.Entry(home)
N2.pack()

ans = tk.StringVar(home)
ans.set("result will be shown here")
BL = tk.Label(home,textvariable = ans)
BL.pack()

Bt = tk.Button(home, text="calculate",command = Calculate)
Bt.pack()

home.mainloop()