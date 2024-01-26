

arr = [1,2,3,4,5,6,7,8,9]

def binarySearch(arr,i,j,x):
    mid = i+(j-i)//2

    if i>j:
        return -1
    
    if arr[mid]== x:
        return mid
    elif arr[mid]>x:
        return binarySearch(arr,i,mid-1,x)
    else:
        return binarySearch(arr,mid+1,j,x)
    
   


if __name__== "__main__":
    print( binarySearch(arr,0,8,18))