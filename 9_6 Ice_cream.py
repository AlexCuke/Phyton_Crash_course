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
class IceCreamStand(Restoraunt):
    def __init__(self,restaraunt_name,cuisine_typ,flavors):
        super().__init__(restaraunt_name,cuisine_typ)
        self.flavors=flavors
    def ice_flavours(self):
        print(f"В реесторане {self.restaraunt_name} подают {self.flavors} мороженое")
IceCreamStand1=IceCreamStand('Волна','9-22','Кофейное')
IceCreamStand1.describe_restaraunt()
IceCreamStand1.ice_flavours()
