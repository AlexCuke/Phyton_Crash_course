from pathlib import Path
path=Path('learning_python.txt')
contents=path.read_text()
contents=contents.rstrip()
print(contents)

contents=path.read_text()
lines=contents.splitlines()
for line in lines:
    print(line)
