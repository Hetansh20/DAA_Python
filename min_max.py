def min_max(arr):
    if(len(arr) == 1) :
        return arr[0], arr[0]
    
    mid = int(len(arr)/2)
    lmin, lmax = min_max(arr[:mid])
    rmin, rmax = min_max(arr[mid:])
    return (min(lmin, rmin), max(lmax, rmax))

arr = [4,6,3,7,9]
ans = min_max(arr)
print(ans)