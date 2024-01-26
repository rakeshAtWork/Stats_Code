#include <bits/stdc++.h>
using namespace std;

long long findFact(int n){
    if(n==0 || n==1)
        return 1;

    return n*findFact(n-1);
}

int main(){

int a=7;

for(int i=1;i<=a;i++){
    if (findFact(i)<=a){
        cout<<i<<" - "<<findFact(i)<<endl;
        // cout<<<<endl;
    }
         
}

return 0;
}