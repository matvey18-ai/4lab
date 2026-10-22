def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")
    return numbers


try:
    validate_numbers([])
except ValueError as error:
    print("Поймано исключение:", error)

try:
    validate_numbers([1.5, 2.5, 3.0])
    print("Список прошёл проверку")
except ValueError as error:
    print("Поймано исключение:", error)
