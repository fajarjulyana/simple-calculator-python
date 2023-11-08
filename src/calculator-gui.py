import tkinter as tk

# Fungsi untuk mengevaluasi ekspresi ketika tombol "=" ditekan
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        result_label.config(text="Hasil: " + result)
    except Exception as e:
        result_label.config(text="Error")

# Membuat jendela aplikasi utama
app = tk.Tk()
app.title("Kalkulator")

# Membuat widget input untuk angka
entry = tk.Entry(app, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Membuat tombol untuk angka dan operator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0

for button in buttons:
    tk.Button(app, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END, b) if b != '=' else evaluate_expression()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Membuat label untuk menampilkan hasil
result_label = tk.Label(app, text="Hasil: ")
result_label.grid(row=row, column=0, columnspan=4)

# Memulai aplikasi GUI
app.mainloop()
