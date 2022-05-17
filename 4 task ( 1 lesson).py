# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое положительное число: '))
n_ost = number % 10
number = number // 10
while number > 0:
    if (number % 10) > n_ost:
        n_ost = number % 10
    number = number // 10
print(n_ost)
