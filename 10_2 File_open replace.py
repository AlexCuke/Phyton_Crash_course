from pathlib import Path
path=Path('learning_python.txt')
contents=path.read_text()
contents.replace('Python','C++')
contents=contents.rstrip()
print(contents)

contents=path.read_text()
for line in contents.splitlines():
    line=line.replace('Python','C++')
    print(line)
