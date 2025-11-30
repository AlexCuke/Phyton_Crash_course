class Restoraunt:
    def __init__(self,restaraunt_name,cuisine_type):
        self.restaraunt_name = restaraunt_name   # сохраняем в атрибут
        self.cuisine_type = cuisine_type         # сохраняем в атрибут

    def describe_restaraunt(self):
        print(self.restaraunt_name,self.cuisine_type)
    def open_restaraunt(self):
        print(self.cuisine_type)
restaurant1=Restoraunt('Волна','9-22')
restaurant1.describe_restaraunt()

restaurant2=Restoraunt('Три орешка','9-18')
restaurant2.describe_restaraunt()

restaurant3=Restoraunt('Дон Марио','12-0')
restaurant3.describe_restaraunt()
