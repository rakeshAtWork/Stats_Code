## Using Divide and Conquer Approach
## Time Complexity : O(n)
## function definition
def findMaxandMin(arr, i, j):
    ## small problem 
    ## single element present in an array
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    ## two element present in an array
    elif i == j - 1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]
    ## big problem -> Divide and Conquer Approach
    else:
        ## Divide
        mid = i + (j-i)//2
        ## Recursion -> conquer
        max_l, min_l = findMaxandMin(arr, i, mid)
        max_r, min_r = findMaxandMin(arr, mid+1, j)
        ## combine
        ## to find the final max_val
        if max_l < max_r:
            max_val = max_r
        else:
            max_val = max_l
        ## to find the final min_val
        if min_l < min_r:
            min_val = min_l
        else:
            min_val = min_r
        
    return max_val, min_val
        
## Driver code
arr = [10, 70, 45, 16, 29, 30, 35, 20, 100000, -2]
i = 0
j = len(arr) - 1
## function calling
max_val, min_val = findMaxandMin(arr, i, j)
print("Maximum and Minimum element in an array is:", max_val, min_val)