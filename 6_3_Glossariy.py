glossariy  ={'String':'строка',
          'Function':'Функция',
          'Turple':'Кортеж, ()',
          'Dictionary':'Словарь, {}',
          'List':'Списокб []'}
print(f"Function: {glossariy.get('Function')}")
print(f"Turple: {glossariy.get('Turple')}")
print(f"Dictionary: {glossariy.get('Dictionary')}")
print(f"Sort: {glossariy.get('Sort', 'Сортирует список')}")
