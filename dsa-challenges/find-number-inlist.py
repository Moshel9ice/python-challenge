def find_number(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1
print(find_number(numbers = [10, 25, 30, 45], target = 30))
print(find_number(numbers = [5, 8, 5, 9], target = 5))
print(find_number(numbers = [10, 20, 30], target = 99))