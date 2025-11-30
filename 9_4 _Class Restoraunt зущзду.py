class Restoraunt:
    def __init__(self,restaraunt_name,cuisine_type):
        self.restaraunt_name = restaraunt_name   # сохраняем в атрибут
        self.cuisine_type = cuisine_type         # сохраняем в атрибут
        self.number_served = 0
    def describe_restaraunt(self):
        print(f"Ресторан: {self.restaraunt_name}, время работы: {self.cuisine_type}, количество поситетелей: {self.number_served}")
    def open_restaraunt(self):
        print(self.cuisine_type)
    def set_number_served(self):
        self.number_served = 10
        
    def increment_number_served(self):
        self.number_served +=2        
restaurant1=Restoraunt('Волна','9-22')
restaurant1.describe_restaraunt()
restaurant1.set_number_served()
restaurant1.increment_number_served()
restaurant1.describe_restaraunt()
restaurant1.increment_number_served()
restaurant1.describe_restaraunt()