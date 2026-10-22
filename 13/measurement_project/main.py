import json
import logging
from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max
from utils.statistics import validate_numbers


def setup_logging(log_file):
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    base_dir = Path(__file__).parent
    config = load_config(base_dir / "config.json")
    setup_logging(base_dir / config["log_file"])

    logging.info("Программа запущена")
    print("Текущий каталог:", Path.cwd())

    input_path = base_dir / config["input_file"]
    print("Файл существует:", input_path.exists())

    try:
        numbers = read_numbers(input_path)
        validate_numbers(numbers)
    except FileNotFoundError:
        logging.error("Файл не найден: %s", input_path)
        print("Ошибка: файл не найден")
        return
    except ValueError as error:
        logging.error("Ошибка данных: %s", error)
        print("Ошибка:", error)
        return

    logging.info("Успешное чтение файла, количество значений: %d", len(numbers))
    print("Количество значений:", len(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))
    print("Среднее:", calculate_average(numbers))
    logging.info("Программа завершена")


if __name__ == "__main__":
    main()
