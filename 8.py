import logging
from pathlib import Path

logs_dir = Path(__file__).parent / "8" / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=logs_dir / "app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("Программа запущена")
logging.info("Файл прочитан, количество значений: 12")
logging.warning("Тестовое предупреждение")
logging.info("Программа завершена")

print("Логи записаны в", logs_dir / "app.log")
