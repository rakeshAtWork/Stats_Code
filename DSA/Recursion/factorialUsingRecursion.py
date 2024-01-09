
# function defination

def factorialFindingRec(n):
    if n == 0:
        return 1
    
    return n*factorialFindingRec(n-1)


# driver code 
n=5

result = factorialFindingRec(n)

print("The result is : ",result)