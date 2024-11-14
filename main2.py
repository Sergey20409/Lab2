salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

for months in range(months):

    money_capital = money_capital + spend - salary
    spend = spend * (1 + increase)
    months += 1
    if months == 10:
        # TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
        print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{money_capital:.2f}")
