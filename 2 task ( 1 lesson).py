# 2 Пользователь вводит время в секундах.
#  Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк.
time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print(f"{hour:02d}:", f"{minute:02d}:", f"{second:02d}")
