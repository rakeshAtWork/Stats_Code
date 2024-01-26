# include<bits/stdc++.h>

using namespace std;


void push(vector<int> &v,int i,int n,int a1,int a2){

    if(i==0||i==1){
        v.push_back(i);
    }

    if(i>n)
        return;
    push(v,i+1,n,a2,a1+a2);


    


}

vector<int> generateFibonacciNumbers(int n) {
    // Write your code here.

    vector<int> ans;

    push(ans, 0,n,0,1);

    return ans;


}


int main(){



    return 0;
}