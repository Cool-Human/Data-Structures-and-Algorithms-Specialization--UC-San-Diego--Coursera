# import random
# import time

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    max_index2 = -1
    for j in range(n):
        if j != max_index1 and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j
    return numbers[max_index1] * numbers[max_index2]

# def generate_random_test():
#     n = random.randint(10,11)
#     arr = [random.randint(10000, 10000000000) for _ in range(n)]
#     return arr

# def stress_test():
#     test_count = 0
#     while True:
#         arr = generate_random_test()

#         start_naive = time.perf_counter()
#         res1 = max_pairwise_product(arr.copy())
#         naive_time = time.perf_counter() - start_naive

#         start_fast = time.perf_counter()
#         res2 = max_pairwise_product_fast(arr.copy())
#         fast_time = time.perf_counter() - start_fast

#         if res1 != res2:
#             print("NOT OKAY")
#             print("Array: {}".format(arr))
#             print("Naive: {}, \n Fast: {}".format(res1, res2))
#             print(f"Time taken: Naive: {naive_time:.6f} sec, Fast: {fast_time:.6f} sec")
#             break
#         else:
#             print(len(arr))
#             print(arr)
#             print("OKAY")
#             print(f"Time taken: Naive: {naive_time:.6f} sec, Fast: {fast_time:.6f} sec")
#             print("Tests passed: {}".format(test_count))
#             test_count += 1
#         if test_count % 10 == 0:
#             print('10 stress tests passed')
#             input("Press Enter to continue...")

if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    
    # if max_pairwise_product(input_numbers) != max_pairwise_product_fast(input_numbers):
    #     print("Wrong answer: {} {}".format(max_pairwise_product(input_numbers), max_pairwise_product_fast(input_numbers)))
    # else:
    #     print('OK \n')

    #stress_test()

    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))