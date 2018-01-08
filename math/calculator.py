def list_avg(numbers):
    sum = list_sum(numbers)
    return sum / numbers.size()


def list_sum(numbers):
    sum = 0

    for next in numbers:
        sum += next

    return sum


def list_min(numbers):
    min_number = numbers[0]

    for next in numbers:
        if next < min_number:
            min_number = next

    return min_number


def list_max(numbers):
    max_number = numbers[0]

    for next in numbers:
        if next > max_number:
            max_number = next

    return max_number
