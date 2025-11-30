def city_country(city, country):
    describe = f"{city}, {country}"
    return describe

print(city_country('Москва', 'Россия'))
print(city_country('Париж', 'Франция'))

while True:
    city = input("Введите город (или 'quit' для выхода): ")
    if city == 'quit':
        break
    country = input("Введите страну: ")
    describe = city_country(city, country)
    print(describe)
