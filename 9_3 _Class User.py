class User:
    def __init__(self,first_name,last_name,age,date_of_registrtion):
        self.first_name = first_name   # сохраняем в атрибут
        self.last_name = last_name         # сохраняем в атрибут
        self.age = age   # сохраняем в атрибут
        self.date_of_registrtion = date_of_registrtion         # сохраняем в атрибут
    def  describe_user(self):
        print(self.first_name,self.last_name,self.age,self.date_of_registrtion)
    def greet_user(self):
        print(f"Добрый день, {self.first_name} {self.last_name}!")
user1=User('Борис','Годунов','37','12.07.2024')
user1.describe_user()
user1.greet_user()
user2=User('Иван','Лизан','30','30.06.2023')
user2.describe_user()
user2.greet_user()
user3=User('Михаил','Романов','22','15.05.2025')
user3.describe_user()
user3.greet_user()
user4=User('Семен','Слепаков','49','22.10.2024')
user4.describe_user()
user4.greet_user()

