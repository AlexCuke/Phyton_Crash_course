fav_numbers  ={'Катя':[7],
          'Саша':[7,5],
          'Леша':[3],
          'Миша':[9],
          'Алиса':[12,7]}
print(fav_numbers['Катя'])
print(fav_numbers.get('Саша'))
print(fav_numbers.get('Вова',[22]))
print(fav_numbers.get('Алиса'))
