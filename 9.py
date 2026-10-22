import json
from pathlib import Path

config_path = Path(__file__).parent / "9" / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)

print("Путь к файлу измерений:", config["input_file"])
print("Путь к журналу логов:", config["log_file"])
