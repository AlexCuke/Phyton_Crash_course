pizzas=['Мясная','Рыбная','Пеперони','Грибная','Гавайская','Острая','С креветкой']
for pizza in pizzas:
    print(f"Я люблю пиццу {pizza}!")
friend_pizzas=pizzas.copy()
friend_pizzas.append('Пикантная')
print(f"Мои любимые пиццы:")
for pizza in pizzas:
    print(pizza)
print(f"Любымые пиццы моего друга:")
for pizza in friend_pizzas:
    print(pizza)