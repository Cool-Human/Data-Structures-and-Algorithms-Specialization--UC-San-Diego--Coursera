def majority_element_naive(elements):
    elements.sort()
    majority_count = len(elements) // 2
    # After sorting, majority element (if exists) is always at middle position
    middle_element = elements[majority_count]
    if elements.count(middle_element) > majority_count:
        return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
