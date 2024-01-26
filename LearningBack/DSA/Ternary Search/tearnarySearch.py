
def ternarySearch(arr,l,r,x):
    
    while(l<=r):
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        
        if arr[mid1] == x :
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif arr[mid1] > x:
            return ternarySearch(arr,l,mid1-1,x)
        elif arr[mid2] < x:
            return ternarySearch(arr,mid2+1,r,x)
        else:
            return ternarySearch(arr,mid1+1,mid2-1,x)
    
    return -1
        
        
    

# driver code 

arr = [1,2,3,4,5,6,7,8,9,10]

l = 0
r= len(arr)-1

x= 7

result = ternarySearch(arr,l,r,x) # function calling.



print("Searching element present at index : ",result)