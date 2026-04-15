rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "RUB": 92.0,
    "KGS": 89.0
}

while True:
    amount = input("Сумма (или q для выхода): ")
    if amount.lower() == "q":
        break

    amount = float(amount)
    from_cur = input("Из валюты: ").upper()
    to_cur = input("В валюту: ").upper()

    if from_cur not in rates or to_cur not in rates:
        print("Неизвестная валюта")
        continue

    result = (amount / rates[from_cur]) * rates[to_cur]
    print("Результат:", result)
    print("-" * 20)
