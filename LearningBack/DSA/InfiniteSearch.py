def binarySearch(arr,i,j,ele):
    while(i<=j):
        mid = i + (j-i)//2
        if arr[mid]=='infinite':
            
            if arr[mid-1]=='infinite':
                print("chk")
                return binarySearch(arr,i,mid-1,ele)
            return mid
        else :
            print("chk")
            return binarySearch(arr,mid+1,j,ele)
    

 

## driver code 
arr = [1,2,3,'infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite','infinite']
ele = 'infinite'
i=0
j=len(arr)
print(j)
result = binarySearch(arr,i,j,ele)
print(f'Element found at {result}')