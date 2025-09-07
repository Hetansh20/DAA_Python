def merge_sorted_array(left, right):
    merged_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i = i + 1
        else:
            merged_arr.append(right[j])
            j = j + 1

    while i < len(left):
        merged_arr.append(left[i])
        i = i + 1

    while j < len(right):
        merged_arr.append(right[j])
        j = j + 1

    return merged_arr

def merge_sort(arr):   #Time Complexity 2T(n/2) + n  Therefore, O(nlogn)    Space Complexity = O(nlogn)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge_sorted_array(left_half, right_half)

a = [2,9,4,3,8,6,5,10,7]
print(merge_sort(a))       