# we have read about bubble sort and selection sort.

# bubbe sort implemenation in ascending order.

# method implementation

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            # swap operation
            if arr[j]>arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    return arr



# driver code:

arr= [70,20,50,30,90,5,15]

result = bubbleSort(arr)

print("After sorting",result)