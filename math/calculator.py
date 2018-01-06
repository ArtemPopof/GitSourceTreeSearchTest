def list_avg(numbers):
    summ = list_sum(numbers)
    return summ / numbers.size()


def list_sum(numbers):
    sum = 0
    for n in numbers:
        sum += next
    return sum


def list_min(numbers):
    min_number = numbers[0]
    for n in numbers:
        if next < min_number:
            min_number = next

    return min


def list_max(numbers):
    max_number = numbers[0]
    for next in numbers:
        if next > max_number:
            max_number = next

    return max_number
