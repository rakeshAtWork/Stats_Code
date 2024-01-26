# Take an array and insert some element in it.
# Just take one key value and try to find the index of that element.
# If the element is present then return its index other retuern -1 that signifies element is not there in the given array.

def linearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1

list1=[12,521,52,22,325,2152,252,32,32,252,22,4878,95]

print(linearSearch(list1,95))