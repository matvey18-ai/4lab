def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")
    return numbers
