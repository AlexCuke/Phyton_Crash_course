peoples  =[{'name':'Александр',
          'surname':'Пушкин',
          'profession':'Поэт',
          'Country':'Российская империя',
          'place of birth':'Москва'},
            {'name':'Николай',
          'surname':'Гоголь',
          'profession':'Писатель',
          'Country':'Российская империя',
          'place of birth':'Сорочинцы'},
            {'name':'Владимир',
          'surname':'Маяковский',
          'profession':'Поэт',
          'Country':'СССР',
          'place of birth':'Багдати'}]
for people in peoples:
    print(people.get('name'), people.get('surname'))
