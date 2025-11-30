responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
 # Запрос имени и ответа пользователя.
 name = input("\nКак Ваше имя? ")
 response = input("Где бы вы Хотели провести отпуск мечты? ")
 # Ответ сохраняется в словаре.
 responses[name] = response
 # Проверка продолжения опроса.
 repeat = input("Продолжить?")
 if repeat == 'нет':
    polling_active = False
# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(f"{name} хотеч провести отпуск мечты в  {response}.")