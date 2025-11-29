favorite_places={'Москва': [{'name':'Александр',
                            'surname':'Пушкин',
                            'profession':'Поэт',
                            'Country':'Российская империя',
                              'place of birth':'Москва'},
                            {'name':'Владимир',
                            'surname':'Маяковский',
                            'profession':'Поэт',
                            'Country':'СССР',
                            'place of birth':'Багдати'}],
                    'Санкт-Петербург':[{'name':'Александр',
                            'surname':'Пушкин',
                            'profession':'Поэт',
                            'Country':'Российская империя',
                              'place of birth':'Москва'}, 
                              {'name':'Николай',
                              'surname':'Гоголь',
                                  'profession':'Писатель',
                               'Country':'Российская империя',
                              'place of birth':'Сорочинцы'}],
                    'Царское село':[
                          {'name':'Александр',
                          'surname':'Пушкин',
                          'profession':'Поэт',
                          'Country':'Российская империя',
                            'place of birth':'Москва'}]}
for city, peoples in favorite_places.items():
    print('Город:', city)
    for people in peoples:
      print(people.get('name'), people.get('surname'))
      
'''favorite_places = {
    'Москва': [
        {'name': 'Александр', 'surname': 'Пушкин'},
        {'name': 'Владимир', 'surname': 'Маяковский'}
    ],
    'Санкт-Петербург': [
        {'name': 'Александр', 'surname': 'Пушкин'},
        {'name': 'Николай', 'surname': 'Гоголь'}
    ],
    'Царское село': [
        {'name': 'Александр', 'surname': 'Пушкин'}
    ]
}'''

people_places = {}

for city, peoples in favorite_places.items():
    for p in peoples:
        full_name = f"{p['name']} {p['surname']}"
        # если человека ещё нет в словаре — создаём запись
        if full_name not in people_places:
            people_places[full_name] = []
        # добавляем город в список его мест (избегаем дубликатов)
        if city not in people_places[full_name]:
            people_places[full_name].append(city)

for person, places in people_places.items():
    print(person, '—', ', '.join(places))