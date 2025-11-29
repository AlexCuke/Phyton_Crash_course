students  ={'Майк':'С++',
          'Иван':'С',
          'Николай':'Java',
        }
names=['Майк','Иван','Валерий','Антон','Николай']
for name in names:
    if  name in students.keys():
        print(f"{name} спасибо за участие в опросе")
    else:
        print(f"{name} примите участие в опросе")
