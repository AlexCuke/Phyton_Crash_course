from user_admin3 import User

class Admin(User):
    def __init__ (self,first_name,last_name,age,date_of_registrtion):
        super().__init__(first_name,last_name,age,date_of_registrtion)
        self.privileges=["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]
    def show_privileges(self):
        print(f"Привелегии: {self.privileges}")


