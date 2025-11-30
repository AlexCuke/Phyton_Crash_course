while True:
    old = input("\nВведитье своей возраст: ")
    if old == 'quit':
        print("Заказ завершён.")
        break
    elif int(old) < 3:
        print("\nБилет бесплатный")
    elif int(old) < 12:
        print("\nБилет стоит 10 долларов")
    else :
        print("\nБилет стоит 15 долларов")

