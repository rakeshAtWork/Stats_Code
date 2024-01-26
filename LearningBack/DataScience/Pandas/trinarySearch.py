def ternary_search(arr, ele, left, right):
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    while left <= right:
        print("if exc")
        if arr[mid1] == ele:
            return "Element found at ", mid1
        elif arr[mid2] == ele:
            return "Element found at ", mid2
        elif arr[mid1] > ele:
            return ternary_search(arr, ele, left, mid1-1 )
        elif arr[mid2] < ele:
            return ternary_search(arr, ele, mid2+1 , right)
        else:
            return ternary_search(arr, ele, mid1+1 , mid2-1 )

    return "Element not present"



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15]
ele = 7

print(ternary_search(arr, ele, 0, len(arr) - 1))

print("hello")