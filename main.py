import tkinter as tk
from tkinter import ttk, messagebox

# Курсы валют
rates = {
    "USD": 1,
    "KGS": 89,
    "EUR": 0.92,
    "RUB": 95,
    "KZT": 450
}

# Конвертация
def convert():
    try:
        amount = float(entry.get())

        if amount <= 0:
            messagebox.showerror("Ошибка", "Введите сумму больше 0")
            return

        result = amount / rates[from_cur.get()] * rates[to_cur.get()]
        result_label.config(text=round(result, 2))

    except:
        messagebox.showerror("Ошибка", "Введите число")

# Смена валют
def swap():
    a = from_cur.get()
    from_cur.set(to_cur.get())
    to_cur.set(a)

# Окно
root = tk.Tk()
root.title("Конвертер")
root.geometry("300x250")

# Выбор валют
from_cur = ttk.Combobox(root, values=list(rates), state="readonly")
from_cur.pack()
from_cur.set("USD")

to_cur = ttk.Combobox(root, values=list(rates), state="readonly")
to_cur.pack()
to_cur.set("KGS")

# Кнопки
ttk.Button(root, text="↔", command=swap).pack()
entry = ttk.Entry(root)
entry.pack()
ttk.Button(root, text="Конвертировать", command=convert).pack()

# Результат
result_label = ttk.Label(root, text="...")
result_label.pack()

root.mainloop()
