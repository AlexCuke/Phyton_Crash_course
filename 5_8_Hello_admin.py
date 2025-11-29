users=['Alex','user_77','Kate','Super1','Agent007','admin','superpeper','Ilimdar']
for user in users:
    if user=='admin':
        print(f'Здравствуйте, {user}, хотите проверить отчет о состоянии дел в системе?')
    else:
        print(f'Привет, {user}, спасибо что авторизировался в системе')
