from functools import cmp_to_key

def largest_number(numbers):
    # Convert to strings for concatenation comparison
    numbers = list(map(str, numbers))
    # Sort using custom comparator: a before b if a+b > b+a
    numbers.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
    # Join and remove leading zeros, return '0' if all zeros
    result = ''.join(numbers).lstrip('0')
    return result if result else '0'


if __name__ == '__main__':
    _ = int(input())  # Read n (unused)
    input_numbers = input().split()  # Read numbers as strings
    print(largest_number(input_numbers))