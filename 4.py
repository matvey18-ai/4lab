from pathlib import Path


def read_numbers(file_path):
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(float(line))
    return numbers


path = Path(__file__).parent / "4" / "data" / "measurements.txt"
numbers = read_numbers(path)
print("Прочитано значений:", len(numbers))
print(numbers)
