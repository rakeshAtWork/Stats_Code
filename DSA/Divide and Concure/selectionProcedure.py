print("will be to print all about selection Procedure.")

def partition(arr,p,q):
    i=p
    pivot = arr[p]

    for j in range(i+1,q+1):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[p]=arr[p],arr[i]

    return i+1

def selectionProcedure(arr,p,q,k):
    if len(arr) == 1:
        return arr[p]
    else:
        m= partition(arr,p,q)
        if m ==k:
            return arr[m-1]
        elif m<k:
            return selectionProcedure(arr,m,q,k)
        else:
            return selectionProcedure(arr,p,m-2,k)



# driver code
        
arr =[20,70,50,48,98,12,10,43]

k=2
p=0
q=len(arr)-1
result = selectionProcedure(arr,p,q,k)
print(f"{k} smallest element : {result}")
arr.sort()
print(arr)