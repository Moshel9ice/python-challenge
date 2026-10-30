

def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zero_count = len(numbers) - len(non_zeros)
    return non_zeros + [0] * zero_count

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))