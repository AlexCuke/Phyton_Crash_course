users=['Alex','user_77','Kate','Super1','Agent007','admin','superpeper','Ilimdar']
new_users=users.copy()
for user in users:
    if len(new_users)!=0:
        print(f'Пользователь {user} удален')
        del new_users[-1]
    if len(new_users)==0:
        print(f'Нам нужно добавить несколько пользователей')
