try:
    file = open("missing.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файл не найден")
finally:
    print("Операция завершена")

try:
    number = float("abc")
except ValueError:
    print("Некорректные данные, преобразование в float невозможно")
