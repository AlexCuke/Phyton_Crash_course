import car_functions as cc
car = cc.make_car('Subaru', 'Impreza',
                prefix='WRX',
                Turbo='True')
print(car)
car=cc.make_car('Reno', 'logan', Value='1.6',power='100')
print(car)
car=cc.make_car('Mazda', '3', Value='2.3',power='260',prefix='WRX',Turbo='True')
print(car)
car=cc.make_car('Mitsubisi', 'ASX',Value='2.3',power='260', variator='True')
print(car)
