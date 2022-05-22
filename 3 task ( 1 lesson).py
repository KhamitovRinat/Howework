# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
vvod_n = input('Введите число: ')
n = int(vvod_n)
nn = int(f'{vvod_n}{vvod_n}')
nnn = int(f'{vvod_n}{vvod_n}{vvod_n}')
summ_n = n + nn + nnn
print(summ_n)
