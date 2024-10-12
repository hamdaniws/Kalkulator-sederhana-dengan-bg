import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')
window.geometry("300x400")  # Set window size to control layout


frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack(expand=True, fill="both")

# Configure row and column expansion in the frame
for i in range(4):
    frame.grid_columnconfigure(i, weight=1, uniform="equal")
for j in range(6):
    frame.grid_rowconfigure(j, weight=1, uniform="equal")

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=5, sticky="nsew")

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

# Button creation with larger font and equal column/row expansion
button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(1))
button_1.grid(row=1, column=0, sticky="nsew")

button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(2))
button_2.grid(row=1, column=1, sticky="nsew")

button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(3))
button_3.grid(row=1, column=2, sticky="nsew")

button_add = tk.Button(master=frame, text="+", padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('+'))
button_add.grid(row=1, column=3, sticky="nsew")

button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(4))
button_4.grid(row=2, column=0, sticky="nsew")

button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(5))
button_5.grid(row=2, column=1, sticky="nsew")

button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(6))
button_6.grid(row=2, column=2, sticky="nsew")

button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('-'))
button_subtract.grid(row=2, column=3, sticky="nsew")

button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(7))
button_7.grid(row=3, column=0, sticky="nsew")

button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(8))
button_8.grid(row=3, column=1, sticky="nsew")

button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(9))
button_9.grid(row=3, column=2, sticky="nsew")

button_multiply = tk.Button(master=frame, text="x", padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('*'))
button_multiply.grid(row=3, column=3, sticky="nsew")

button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, font=("Arial", 14), command=clear)
button_clear.grid(row=0, column=3, sticky="nsew")

button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick(0))
button_0.grid(row=4, column=0, columnspan=1, sticky="nsew")

button_00 = tk.Button(master=frame, text='00', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('00'))
button_00.grid(row=4, column=1, columnspan=2, sticky="nsew")

button_div = tk.Button(master=frame, text="/", padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('/'))
button_div.grid(row=4, column=3, sticky="nsew")

button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, font=("Arial", 14), command=equal)
button_equal.grid(row=5, column=0, sticky="nsew", ipadx=10, ipady=10, columnspan=3)

button_coma = tk.Button(master=frame, text=',', padx=15, pady=5, font=("Arial", 14), command=lambda: myclick('.'))
button_coma.grid(row=5, column=3, sticky="nsew")

window.mainloop()
