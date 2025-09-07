def partition(arr, low, high):
    pivot = arr[high]
    pindex = low
    for i in range(low, high):
        if(arr[i] < pivot):
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex = pindex + 1
            
    arr[high], arr[pindex] = arr[pindex], arr[high]
    return pindex

def quick_sort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = [2, 8, 9, 3, 1, 7, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)