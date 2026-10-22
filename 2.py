def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


numbers = [12.5, 9.8, 14.2, 11.0, 13.6, 10.4, 15.1, 8.9, 12.0, 11.7]
print("Среднее:", calculate_average(numbers))
print("Минимум:", find_min(numbers))
print("Максимум:", find_max(numbers))
