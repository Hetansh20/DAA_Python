# Insertion Sort
# Insertion Sort also known as in-place sorting algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [4, 5, 3, 1, 2, 8]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)