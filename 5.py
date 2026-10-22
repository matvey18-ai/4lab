from pathlib import Path

print("Текущий рабочий каталог:", Path.cwd())

file_path = Path(__file__).parent / "4" / "data" / "measurements.txt"
print("Путь к файлу:", file_path)
print("Файл существует:", file_path.exists())

logs_dir = Path(__file__).parent / "5" / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)
print("Каталог logs создан:", logs_dir.exists())
