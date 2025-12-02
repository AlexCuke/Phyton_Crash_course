
from pathlib import Path
import json
path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)
print(f"Your favorite number is {number}!")