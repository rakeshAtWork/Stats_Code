#include<bits/stdc++.h>
class Solution {
public:
   unsigned long mySqrt(int x) {

       if (x == 0 || x == 1)
            return x;
   unsigned long ans =0;
    int i = 1;
    int j = x;
    unsigned long mid = -1;

    while(i<=j){
        mid = i+(j-i)/2;
        //unsigned long sq = mid*mid;
        if( mid*mid >x){
            j= mid - 1;
            
        }else if( mid*mid ==x){
          return mid;
        }else{
            i = mid + 1;
        }

    }

    return j;
            
    }

    

    
};