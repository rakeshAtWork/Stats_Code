# merge procedure

def mergeProcedure(arr,i,mid,j):
    # number of element in left subarray
    n1 = mid -i+1
    # number of element in right subarray
    n2 = j-mid

    leftSubarray = [0]*n1
    rightSubaar = [0]*n2

    # copying elemnt from array to subarrays

    for m in range(n1):
        leftSubarray[m]=arr[i+m]
    for n in range(n2):
        rightSubaar[n]=arr[mid+1+n]

    p=0
    q=0
    k=i
    while p<n1 and q<n2:
        if leftSubarray[p]<=rightSubaar[q]:
            arr[k]=leftSubarray[p]
            p+=1
        else:
            arr[k]= rightSubaar[q]
            q+=1
        k+=1

    # copy remaning element from left subarray
        
    while p<n1:
        arr[k]=leftSubarray[p]
        p+=1
        k+=1
    # copy remaning element from right sub array
    while q<n2:
        arr[k]= rightSubaar[q]
        q+=1
        k+=1


# merger sort function implementation

def mergeSort(arr,i,j):
    if i<j:
        # divide
        mid = i+(j-i)//2
        mergeSort(arr,i,mid)
        mergeSort(arr,mid+1,j)
        mergeProcedure(arr,i,mid,j)
    return arr

#diver code
arr =[50,70,65,13,8,62,98,27]
i = 0
j = len(arr) -1
# function calling
result = mergeSort(arr,i,j)
print("Array after sorting : ",result)

