
from pathlib import Path
import json
user_remember={'Name':'','Age':'','Sex':''}
def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        user_remember = json.loads(contents)
        username=user_remember['Name']
        return username
    else:
        return None
def get_new_username():  
    user_remember['Name'] = input("What is your correct name? ") 
    path = Path('username1.json')
    contents = json.dumps(user_remember)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {user_remember['Name']}!")
def greet_user():
    path = Path('username1.json')
    username= get_stored_username(path)
    if username:
        ask=input((f"Правильно ли определено твое имя {username}?"))
        if ask == 'y':
            print(f"Welcome back, {username}!")
        else:
            get_new_username()
    else:
        user_remember['Name'] = input("What is your name? ")
        user_remember['Age'] = input("How iold are you? ")
        user_remember['Sex'] = input("What is your sex? ")
        ask=input(f"Правильно ли определено твое имя {user_remember['Name']}?")
        contents = json.dumps(user_remember)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {user_remember['Name']}!")
greet_user()