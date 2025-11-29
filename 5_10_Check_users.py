current_users=['Alex','user_77','Kate','Super1','Agent007','admin','superpeper','Ilimdar']
new_users=['michaul','pAul','six','claud','user_77','Super1','Otar','Jonh']
current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
print(current_users_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Имя {new_user} занято')
    else:    
        print(f'Имя {new_user} доступно')