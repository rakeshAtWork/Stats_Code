
def infiniteSearch(arr,i,j):
    
    mid = i+(j-i)//2
    
    while(i<j):
        if arr[mid]=="inf":
            if arr[mid-1]=='inf':
                
                return infiniteSearch(arr,i,mid-1)
            else:
                return mid
        else:
            return infiniteSearch(arr,mid+1,j)
            
        
    
    

if __name__=="__main__":
    
    print("Hello")
    
    arr= [20,-30,10,5,7,0,29,"inf",'inf',"inf","inf","inf",'inf',"inf","inf"]

    ans = infiniteSearch(arr,0,len(arr))
    
    print("This is the position of first infinite position : ", ans,end="")
    
    
