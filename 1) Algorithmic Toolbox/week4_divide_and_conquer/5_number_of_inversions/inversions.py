def inversions_naive(a):
    """Count inversions in O(n log n) using merge sort."""
    def merge_count_helper(arr, temp, left, mid, right):
        i = left      # Left subarray pointer
        j = mid + 1   # Right subarray pointer
        k = left      # Temp array pointer
        inv_count = 0
        
        # Merge and count inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                # All elements arr[i:mid+1] are inversions with arr[j]
                temp[k] = arr[j]
                inv_count += mid - i + 1
                j += 1
            k += 1
        
        # Copy remaining elements
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back to original array
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            inv_count += merge_count_helper(arr, temp, left, mid, right)
        return inv_count
    
    arr_copy = a[:]  # Work on a copy to avoid modifying original
    temp = [0] * len(a)
    return merge_sort_count(arr_copy, temp, 0, len(a) - 1)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))