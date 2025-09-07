def occurence(arr,ele):
    count =0
    for i in range(len(arr)):
        if(ele==arr[i]):
            count+=1
    return count

arr=[1,2,3,2,5,3,2]
key=2
print(occurence(arr,key))