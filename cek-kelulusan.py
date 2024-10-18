import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL for image handling

def cek_kelulusan():
    try:
        # Get values from input fields
        nilai_bahasa = int(entry_bahasa.get())
        nilai_matematika = int(entry_matematika.get())
        nilai_ipa = int(entry_ipa.get())

        # Calculate total and average
        total_nilai = nilai_bahasa + nilai_matematika + nilai_ipa
        rata_rata = total_nilai / 3
        kelulusan = 'Lulus' if rata_rata >= 60 else 'Tidak Lulus'

        # Update result labels
        label_total_nilai.config(text=f"Total Nilai: {total_nilai}")
        label_rata_rata.config(text=f"Rata - Rata: {rata_rata:.2f}")
        label_kelulusan.config(text=f"Kelulusan: {kelulusan}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# Create the main window
root = tk.Tk()
root.title("Cek Kelulusan")

# Activate fullscreen mode
root.attributes('-fullscreen', True)

# Load and set the background image
bg_image = Image.open("BlueAikatsu.png")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)  # Resize to fit the screen
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
label_bg = tk.Label(root, image=bg_photo)
label_bg.place(relwidth=1, relheight=1)  # Make the label fill the entire window

# Create a frame for the content
frame = tk.Frame(root, bg='black', padx=30, pady=30)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame

# Create input fields with left alignment
label_bahasa = tk.Label(frame, text="Masukkan Nilai Bahasa Indonesia:", bg='black', fg='white', anchor='w')
label_bahasa.pack(anchor='w', pady=5)
entry_bahasa = tk.Entry(frame, width=30)  # Set width for the text box
entry_bahasa.pack(anchor='w', pady=5)

label_matematika = tk.Label(frame, text="Masukkan Nilai Matematika:", bg='black', fg='white', anchor='w')
label_matematika.pack(anchor='w', pady=5)
entry_matematika = tk.Entry(frame, width=30)  # Set width for the text box
entry_matematika.pack(anchor='w', pady=5)

label_ipa = tk.Label(frame, text="Masukkan Nilai IPA:", bg='black', fg='white', anchor='w')
label_ipa.pack(anchor='w', pady=5)
entry_ipa = tk.Entry(frame, width=30)  # Set width for the text box
entry_ipa.pack(anchor='w', pady=5)

# Create button to check passing status
button_cek = tk.Button(frame, text="Cek Kelulusan", command=cek_kelulusan, anchor='w')
button_cek.pack(pady=10)

# Create labels for results
label_total_nilai = tk.Label(frame, text="Total Nilai: ", bg='black', fg='white')
label_total_nilai.pack(anchor='w', pady=5)

label_rata_rata = tk.Label(frame, text="Rata - Rata: ", bg='black', fg='white')
label_rata_rata.pack(anchor='w', pady=5)

label_kelulusan = tk.Label(frame, text="Kelulusan: ", bg='black', fg='white')
label_kelulusan.pack(anchor='w', pady=5)

# Bind to activate and deactivate fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

# Run the application
root.mainloop()