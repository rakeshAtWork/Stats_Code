# given a sorted array and we need to return a pair of indexes whose value sum is equal to given target value.

#function defination

def parSum(arr,target):
    i=0
    j=len(arr)-1

    while(i<j):
        if(arr[i]+arr[j]==target):
            return i,j
        elif (arr[i] + arr[j]>target):
            j=j-1
        else:
            i=i+1
    
    return -1,-1


# Driver Code

arr =[10,20,30,45,55,57,60]

target = 39

result = parSum(arr,target)

print("The result is : ",result)
