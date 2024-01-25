# partition function implementation
def partition(arr,p,q):
    i=p
    # strarting element as pivot element.
    pivot = arr[p]
    for j in range(i+1,q+1):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    # swap between arr[i] and pivot element.
    arr[i],arr[p] = arr[p],arr[i]
    return i

# quick sort implementation
def quickSort(arr,p,q):
    if p<q:
        mid = partition(arr,p,q)
        quickSort(arr,p,mid-1)
        quickSort(arr,mid+1,q)
    return arr
# driver code
arr = [20,10,5,70,50,89,34]
p=0
q=len(arr)-1
# function calling
result = quickSort(arr,p,q)
print("sorted array after applying the quick sort is: ",result)