# Analysis:
# Time and Space Complexity:

# prit sum

def sum_of_number(lst):
    sum=0
    for x in lst:
        sum+=x
    return sum

lst=[10,5,20,78,52]
result= sum_of_number(lst)
print(result)
