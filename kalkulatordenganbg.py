import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter.constants import SUNKEN


# Membuat window utama
window = tk.Tk()
window.title('Calculator')

# Aktifkan mode fullscreen
window.attributes('-fullscreen', True)

# Membaca gambar background menggunakan PIL
bg_image = Image.open("BlueAikatsu.png")
bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Membuat Canvas untuk background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Frame di atas canvas
frame = tk.Frame(master=window, bg="blue", padx=2)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Tempatkan frame di tengah layar

# Entry field
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=10, font=(500), width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2, sticky="nsew")

# Fungsi untuk memasukkan angka ke dalam entry
def myclick(number):
    entry.insert(tk.END, number)

# Fungsi untuk menghitung hasil
def equal():
    try:
        expression = entry.get()
        # Replace the unicode multiplication and division signs if any
        expression = expression.replace('×', '*').replace('÷', '/')
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Fungsi untuk membersihkan entry
def clear():
    entry.delete(0, tk.END)

# Fungsi untuk menghapus karakter terakhir
def delete_last_char():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

# Fungsi untuk memasukkan kurung ke dalam entry
def insert_paren():
    current_text = entry.get()
    if current_text.count('(') > current_text.count(')'):
        entry.insert(tk.END, ')')
    else:
        entry.insert(tk.END, '(')

# Fungsi untuk memasukkan tanda negatif
def insert_neg():
    entry.insert(tk.END, '-')

# Fungsi untuk menghitung pangkat
def pangkat():
    current_text = entry.get()
    if current_text:  # Cek apakah entry tidak kosong
        entry.insert(tk.END, "**")

# Fungsi untuk menghitung persentase
def percentage():
    try:
        current_text = entry.get()
        if not current_text:
            return

        # Define operators
        operators = ['+', '-', '*', '/']
        last_operator_pos = -1
        last_operator = ''

        # Find the last operator in the expression
        for op in operators:
            pos = current_text.rfind(op)
            if pos > last_operator_pos:
                last_operator_pos = pos
                last_operator = op

        if last_operator_pos == -1:
            # No operator found, treat the entire number as a percentage
            number = float(current_text)
            result = str(number * 0.01)
        else:
            # Get the number before and after the last operator
            before_op = current_text[:last_operator_pos]
            after_op = current_text[last_operator_pos+1:]

            # Handle cases where there might be multiple operators in a row
            if not before_op:
                # If there's no number before the operator, treat the percentage as 0
                number_before = 0
            else:
                # Extract the last number before the operator
                tokens = before_op.strip().split()
                try:
                    number_before = float(before_op.split()[-1])
                except:
                    # Fallback if splitting by space doesn't work
                    number_before = float(before_op)

            # Extract the last number after the operator
            if not after_op:
                return  # Nothing to convert
            try:
                number = float(after_op)
            except:
                # If the after_op is not a valid number, do nothing
                return

            # Calculate the percentage based on the operator
            if last_operator in ['+', '-']:
                percent_value = number_before * (number / 100)
            elif last_operator in ['*', '/']:
                percent_value = number * 0.01
            else:
                percent_value = number * 0.01  # Default case

            # Replace the last number with the percentage value
            new_expression = current_text[:last_operator_pos+1] + str(percent_value)
            result = new_expression

        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        print(f"Percentage Error: {e}")
        tkinter.messagebox.showinfo("Error", "Syntax Error")


# Pembuatan tombol angka
button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(1))
button_1.grid(row=1, column=1, pady=2, sticky="nsew")
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(2))
button_2.grid(row=1, column=2, pady=2, sticky="nsew")
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(3))
button_3.grid(row=1, column=3, pady=2, sticky="nsew")
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(4))
button_4.grid(row=2, column=1, pady=2, sticky="nsew")
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(5))
button_5.grid(row=2, column=2, pady=2, sticky="nsew")
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(6))
button_6.grid(row=2, column=3, pady=2, sticky="nsew")
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(7))
button_7.grid(row=3, column=1, pady=2, sticky="nsew")
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(8))
button_8.grid(row=3, column=2, pady=2, sticky="nsew")
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(9))
button_9.grid(row=3, column=3, pady=2, sticky="nsew")
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, font=(50), command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2, sticky="nsew", columnspan=2)
button_00 = tk.Button(master=frame, text='00', padx=15, pady=5, width=3, font=(50), command=lambda: myclick('00'))
button_00.grid(row=4, column=3, pady=2, sticky="nsew")

#button kalkulasi
button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, font=(50), command=lambda: myclick('+'))
button_add.grid(row=1, column=4, pady=2, sticky="nsew")
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, font=(50), command=lambda: myclick('-'))
button_subtract.grid(row=2, column=4, pady=2, sticky="nsew")
button_multiply = tk.Button(master=frame, text="x", padx=15, pady=5, width=3, font=(50), command=lambda: myclick('*'))
button_multiply.grid(row=3, column=4, pady=2, sticky="nsew")
button_div = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, font=(50), command=lambda: myclick('/'))
button_div.grid(row=4, column=4, pady=2, sticky="nsew")
button_clear = tk.Button(master=frame, text="c", padx=15, pady=5, width=3, font=(50), command=clear)
button_clear.grid(row=1, column=0, pady=2, sticky="nsew")
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, font=(50), command=equal)
button_equal.grid(row=5, column=1, columnspan=4, pady=2, sticky="nsew")
button_delete_last = tk.Button(master=frame, text="Del", padx=15, pady=5, width=3, font=(50), command=delete_last_char)
button_delete_last.grid(row=0, column=4, pady=2, sticky="nsew")
button_paren = tk.Button(master=frame, text="()", padx=15, pady=5, width=3, font=(50), command=insert_paren)
button_paren.grid(row=2, column=0, pady=2, sticky="nsew")
button_neg = tk.Button(master=frame, text="(-", padx=15, pady=5, width=3, font=(50), command=insert_neg)
button_neg.grid(row=2, column=0, pady=2, sticky="nsew")
button_comma = tk.Button(master=frame, text=".", padx=15, pady=5, width=3, font=(50), command=lambda: myclick('.'))
button_comma.grid(row=3, column=0, pady=2, sticky="nsew")
button_pangkat = tk.Button(master=frame, text="^", padx=15, pady=5, width=3, font=(50), command=pangkat)
button_pangkat.grid(row=4, column=0, pady=2, sticky="nsew")
# Tombol Persentase
button_percentage = tk.Button(master=frame, text="%", padx=15, pady=5, width=3, font=(50), command=percentage)
button_percentage.grid(row=5, column=0, pady=2, sticky="nsew")
# Mengatur grid layout untuk tombol
for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
for j in range(6):
    frame.grid_columnconfigure(j, weight=1)

# Fungsi fullscreen
def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

# Bind untuk mengaktifkan dan menonaktifkan fullscreen
window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

# Jalankan window
window.mainloop()
