class User:
    def __init__(self,first_name,last_name,age,date_of_registrtion):
        self.first_name = first_name   # сохраняем в атрибут
        self.last_name = last_name         # сохраняем в атрибут
        self.age = age   # сохраняем в атрибут
        self.date_of_registrtion = date_of_registrtion         # сохраняем в атрибут
        self.login_attempts=0
    def  describe_user(self):
        print(f"Имя, фамилия: {self.first_name},{self.last_name}, возраст: {self.age},дата регистрации: {self.date_of_registrtion},попыток входа: {self.login_attempts}")
    def greet_user(self):
        print(f"Добрый день, {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0



