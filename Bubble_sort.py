# Bubble Sort
# Space Complexity: O(1)
# Time Complexity: O(n^2)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 3, 8, 1, 2]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
