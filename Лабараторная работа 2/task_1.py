money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while True:
    if money_capital < spend:
        break
    elif month > 1:
        spend = (spend * increase) + spend
    money_capital += salary
    money_capital -= spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
