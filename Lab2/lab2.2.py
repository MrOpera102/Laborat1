import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
all_salary = salary * months
all_spend = 0
for _ in range(months):
    all_spend += spend
    spend *= increase + 1
money_capital = all_spend - all_salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))
