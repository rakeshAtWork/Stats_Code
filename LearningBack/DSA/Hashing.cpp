#include<bits/stdc++.h>
using namespace std;

// Here is the input format:

/*

5               size of array
1 3 2 1 3       Elements of array
5               Number of queries
1               q
4               q
2               q
3               q
12              q

*/

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    // precompute

    int hash[13]={0};
    for(int i=0;i<n;i++){
        hash[arr[i]]+=1;
    }



    int q;
    cin>> q;
    while(q--){
        int number;
        cin>>number;
        // Fetch
        cout<<hash[number]<<endl;
    }



    return 0;
}