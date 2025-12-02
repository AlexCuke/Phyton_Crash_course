def sum_numbers():
    while True:
        first = input('Введите первое число (или q для выхода): ')
        if first == 'q':
            break

        second = input('Введите второе число: ')

        try:
            first_num = int(first)      # преобразуем к int
            second_num = int(second)    # преобразуем к int
            result = first_num + second_num
            print('Сумма:', result)
        except ValueError:
            print('Вы ввели не числа')

sum_numbers()