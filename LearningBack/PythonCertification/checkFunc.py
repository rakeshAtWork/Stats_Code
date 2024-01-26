
fh = open("D:\\EDI Mapping In Python\\Learning\\PythonCertification\\romeo.txt")
lst = list()

for line in fh:
    
    str=line.rstrip()
    
    words=str.split()
    
    for w in words:
        
        if w not in lst:
            lst.append(w)

lst.sort()

print(lst)
    

