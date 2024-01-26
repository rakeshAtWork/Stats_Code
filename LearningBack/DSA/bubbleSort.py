ls=[1,2,3,4,54,5,6]


for x in range(0,len(ls)):
    for j in range(0,x-1):
        if ls[j+1]<ls[j]:
            tmp=ls[j]
            ls[j]=ls[j+1]
            ls[j+1]=tmp
        else:
            break
print(ls)