from pathlib import Path

guest_book=''
while True:
   guest=input("Введите имя гостя ")
   if guest == 'q':
        break
   else:
        guest_book=guest_book+guest+'\n'
path=Path('guest_book.txt')
path.write_text(guest_book)

