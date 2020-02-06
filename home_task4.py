earnings = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
staff = int(input("Введите кол-во сотрудников фирмы: "))
profit = earnings - costs
efficiency = (profit / earnings) * 100
profit_staff = profit / staff
if earnings > costs:
    print("Фирма приносит прибыль")
    print("Рентабельность: ", "%.0f" % efficiency, "процентов")
    print("Прибыль фирмы на одного сотрудника: ", "%.2f" % profit_staff, "рублей")
elif costs > earnings:
    print("Фирма убыточна")


