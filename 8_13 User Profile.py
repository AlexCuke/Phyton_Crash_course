def build_profile(first, last, **user_info):
    """Создает словарь, содержащий информацию о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                location='princeton',
                field='physics')
print(user_profile)
user_profile=build_profile('Michael', 'Lermontov', Profession='Poet')
print(user_profile)
user_profile=build_profile('Ivan', 'Lizan', Profession='Analitic', age=30)
print(user_profile)
user_profile=build_profile('Anna', 'Asti',Profession='Singer', age=30,song='Tsarica',country='Russia')
print(user_profile)
