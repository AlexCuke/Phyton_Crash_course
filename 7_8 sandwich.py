sandwich_orders=['Гамбургер','Чизбургер','Биг Мак','Биг Хит','Фреш Ролл','Шарума','Люля']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"Я приготовил бутерброд с {sandwich}")
print("\nПриготовление бутербродов:")

# По очереди «готовим» бутерброды из готового списка
while finished_sandwiches:
    sandwich = finished_sandwiches.pop()
    print(f"Я приготовил бутерброд с {sandwich}")