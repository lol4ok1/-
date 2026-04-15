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

    # проверка числа
    try:
        amount = float(amount)
    except ValueError:
        print("Ошибка: нужно ввести число!")
        continue

    from_cur = input("Из валюты: ").upper()
    to_cur = input("В валюту: ").upper()

    # проверка валют
    if from_cur not in rates or to_cur not in rates:
        print("не правильная волюта") # Твоя фраза здесь
        print("-" * 20)
        continue

    # Расчет
    result = (amount / rates[from_cur]) * rates[to_cur]
    print("Результат:", round(result, 2))
    print("-" * 20)
