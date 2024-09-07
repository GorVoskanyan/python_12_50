import random 

lucky_number = random.randint(1, 38)

if lucky_number == 37:
    print('Выпавший номер: 0…')
    print('Выигравшая ставка: 0')
elif lucky_number == 38:
    print('Выпавший номер: 00…')
    print('Выигравшая ставка: 00')
else:
    reds = '1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 и 36'
    color = 'черное' if str(lucky_number) not in reds else 'красное'
    even_or_odd = 'нечетное' if lucky_number % 2 != 0 else 'четное'
    numbers_range = 'от 1 до 18' if lucky_number in range(1, 19) else 'от 19 до 36' 
    
    print('Выпавший номер:', lucky_number)
    print('Выигравшая ставка:', lucky_number)
    print('Выигравшая ставка:', color)
    print('Выигравшая ставка:', even_or_odd)
    print('Выигравшая ставка:', numbers_range)
    