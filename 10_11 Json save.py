
from pathlib import Path
import json
def save_json():
    number = input("What is your favorite number? ")
    path = Path('favorite_number1.json')
    contents = json.dumps(number)
    path.write_text(contents)
    print(f"Число сохранено в файле!")
def load_json():
    path = Path('favorite_number1.json')
    contents = path.read_text()
    number = json.loads(contents)
    print(f"Your favorite number is {number}!")
try:
    load_json()     # преобразуем к int

except FileNotFoundError:
    save_json()