#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
#финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
#или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
#прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
#фирмы в расчёте на одного сотрудника.
revenue = int(input('Введите значение выручки: '))
cost = int(input('Введите значение издержки: '))
if revenue > cost:
    print('Прибыль')
    rent_profit = ((revenue - cost) / revenue) * 100
    print('Рентабельность выручки Вашей компании:', rent_profit)
    population = int(input('Численность сотрудников фирмы: '))
    per_pop_profit = (revenue - cost) / population
    print('Прибыль фирмы в расчёте на одного сотрудника:', per_pop_profit)
else:
    print('Убыток')
