#function defination

def calculateMaxMin(arr,i,j):
    
    if i == j:
        max_val= arr[i]
        min_val= arr[i]
        
    elif i == (j-1):
        if arr[i]>arr[j]:
            max_val = arr[i]
            min_val = arr[j]
        else:
            max_val = arr[j]
            min_val = arr[i]
    else:
        mid = i+(j-i)//2
        max_l,min_l= calculateMaxMin(arr,i,mid)
        max_r,min_r= calculateMaxMin(arr,mid+1,j)

        if max_l>max_r:
            max_val= max_l
        else:
            max_val= max_r
        if min_l> min_r:
            min_val = min_r
        else:
            min_val= min_l

    return max_val,min_val


# driver code

arr= [50,10,20,45,12,78,20,45,25,35,655,8,1,552,-9]
i = 0
j = len(arr)-1

max_val,min_val = calculateMaxMin(arr,i,j)

print("The max value is ",max_val," and min value is ",min_val)