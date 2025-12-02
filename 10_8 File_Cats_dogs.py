from pathlib import Path

def open_file(file):
    path=Path(file)
    try:
        contents=path.read_text()
        contents=contents.rstrip()
        print(contents)
    except FileNotFoundError:
        print(f"Файл {file} не найден")



open_file('cats.txt')
open_file('dogs.txt')
open_file('dogs1.txt')