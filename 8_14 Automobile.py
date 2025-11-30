def make_car(manufacturer, model, **user_info):
    """Создает словарь, содержащий информацию о пользователе."""
    user_info['manufacturer'] = manufacturer
    user_info['model'] = model
    return user_info
car = make_car('Subaru', 'Impreza',
                prefix='WRX',
                Turbo='True')
print(car)
car=make_car('Reno', 'logan', Value='1.6',power='100')
print(car)
car=make_car('Mazda', '3', Value='2.3',power='260',prefix='WRX',Turbo='True')
print(car)
car=make_car('Mitsubisi', 'ASX',Value='2.3',power='260', variator='True')
print(car)
