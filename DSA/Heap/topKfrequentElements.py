import heapq
from collections import Counter

# function Defination

def topKfrequentElel(arr,k):
    if k == len(arr):
        return set(arr)
    count = Counter(arr)

    ans = heapq.nlargest(k,count.keys(),key=count.get)

    return ans


# driver code

arr = [1,1,1,1,2,2,2,3]
k=2

res = topKfrequentElel(arr,k)

print("The result is : ",res)
