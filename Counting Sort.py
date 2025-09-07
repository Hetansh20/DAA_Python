# Counting Sort
# Counting Sort is a non-comparison based sorting algorithm
# Time Complexity: O(n)
# Space Complexity: O(n) where n is the range of the input

def counting_sort(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i

    count = [0 for i in range(max_val + 1)]
    for i in arr:
        count[i] += 1

    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)


# HW


