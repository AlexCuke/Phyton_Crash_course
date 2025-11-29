rivers  ={'Egypet':'Nile',
          'Russia':'Volga',
          'USA':'Missisipi',
        }
for key in rivers.keys():
    print(f"{key} страна где протекает {rivers.get(key)}")
for value in rivers.values():
    print(f"{value} река добавлена")
for key in rivers.keys():
    print(f"{key} страна добавлена")
