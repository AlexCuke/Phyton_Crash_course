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
class Privileges():
    def __init__ (self):
       self.privileges=["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"] 
    def show_privileges(self):
        print(f"Привелегии: {self.privileges}")
class Admin(User):
    def __init__ (self,first_name,last_name,age,date_of_registrtion):
        super().__init__(first_name,last_name,age,date_of_registrtion)
        self.privileges=Privileges()
   
admin1=Admin('Борис','Годунов','37','12.07.2024')
admin1.describe_user()
admin1.privileges.show_privileges()

