from  user_admin4 import User
from  user_admin4 import Admin 
   
admin1=Admin('Борис','Годунов','37','12.07.2024')
admin1.describe_user()
admin1.show_privileges()


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