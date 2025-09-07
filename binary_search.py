def binary_search(arr, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, right, key)
        else:
            return binary_search(arr, left, mid - 1, key)
    else:
        return -1
    
arr = [2,4,5,6,7,8,9]
left = 0
right = len(arr)
key = 7
print(binary_search(arr,left,right,key))