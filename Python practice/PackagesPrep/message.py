from importlib.resources import path
from pathlib import Path

# path = Path("emails")
# print(path.exists())


path = Path()
for file in path.glob('*.json'):
    print(file)
    