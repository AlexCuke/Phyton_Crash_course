from pathlib import Path
guest=input("Введите имя гостя ")

path=Path('guest.txt')
path.write_text(guest)

