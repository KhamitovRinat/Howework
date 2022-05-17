# 1 Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.
# 1 part
name = 'Rinat'
age = 27
bornplace = 'Kazan'
office = 'FPD RT'
print('My name is ', name, ',', age, ' years old,', " from ", bornplace, ' , working in ', office, '.')

# 2 part
name = input('Введите ваше имя: ')
born_date = int(input('Введите ваш год рождения: '))
current_year = 2022
age = current_year - born_date
city = input('Введите Ваш город: ')
print('Дорогой', name, ', Вы живёте в прекрасном городе', city, ', и Вам', age, 'лет!')
