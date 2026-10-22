from pathlib import Path

base = Path(__file__).parent / "1" / "measurement_project"
folders = ["utils", "data", "logs"]
files = ["main.py", "config.json", ".gitignore", "utils/__init__.py", "utils/reader.py", "utils/statistics.py"]

for folder in folders:
    (base / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = base / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()

print("Структура проекта measurement_project создана:")
for path in sorted(base.rglob("*")):
    print(" ", path.relative_to(base.parent))
