#include<bits/stdc++.h>

using namespace std;

int main(){

    unordered_set<int> s;
    s.insert(10);
    s.insert(20);


    cout << s.count(20)<<endl; // Check Element is Present or Not.

    if(s.find(10)!=s.end()){
        cout<<"Element is Present.";
    }else{
        cout<<"Not Present.";
    }

    return 0;
}
