import tkinter as tk
from tkinter import ttk, messagebox

rates = {
    "USD": 1,
    "KGS": 89,
    "EUR": 0.92,
    "RUB": 95,
    "KZT": 450
}


def convert():
    try:
        amount = float(entry_amount.get())

        if amount <= 0:
            messagebox.showerror("Ошибка", "Сумма должна быть больше 0!")
            return

        cur1 = combo_from.get()
        cur2 = combo_to.get()

        if not cur1 or not cur2:
            messagebox.showerror("Ошибка", "Выбери валюту!")
            return

        result = amount / rates[cur1] * rates[cur2]

        label_result.config(text=f"{amount} {cur1} = {round(result, 2)} {cur2}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите число!")


def swap():
    cur1 = combo_from.get()
    cur2 = combo_to.get()
    combo_from.set(cur2)
    combo_to.set(cur1)
root = tk.Tk()
root.title("Конвертер валют 💱")
root.geometry("320x300")
root.resizable(False, False)
ttk.Label(root, text="Конвертер валют", font=("Arial", 14)).pack(pady=10)
ttk.Label(root, text="Из валюты:").pack()
combo_from = ttk.Combobox(root, values=list(rates.keys()), state="readonly")
combo_from.pack()
combo_from.set("USD")
ttk.Label(root, text="В валюту:").pack()
combo_to = ttk.Combobox(root, values=list(rates.keys()), state="readonly")
combo_to.pack()
combo_to.set("KGS")
ttk.Button(root, text="↔ Поменять валюты", command=swap).pack(pady=5)
ttk.Label(root, text="Сумма:").pack()
entry_amount = ttk.Entry(root)
entry_amount.pack()
ttk.Button(root, text="Конвертировать", command=convert).pack(pady=10)
label_result = ttk.Label(root, text="Результат появится здесь", font=("Arial", 10))
label_result.pack(pady=10)
root.mainloop()
