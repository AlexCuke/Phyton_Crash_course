num=input('На сколько мест бронировать столик? ')
num=int(num)
if num > 8 :
    print(f"Вам придется подождать")
else:
    print("Стол готов")