sandwich_orders=['Гамбургер','Чизбургер pastrami','Биг Мак','Биг Хит pastrami','Фреш Ролл','Шарума pastrami','Люля']
finished_sandwiches=[]
active=True
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    if sandwich.count('pastrami')==0:
        finished_sandwiches.append(sandwich)


while finished_sandwiches:
    sandwich = finished_sandwiches.pop()
    print(f"Я приготовил бутерброд с {sandwich}")