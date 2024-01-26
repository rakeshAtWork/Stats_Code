# include<bits/stdc++.h>
using namespace std;

void revA(string &v ,int l,int r){

    if(l>r)
        return;

    char t= v[r];
    v[r]=v[l];
    v[l]=t;
    revA(v,l+1,r-1);


}

bool isPalindrome(string& str) {
    // Write your code here.
    string org=str;
    revA(str,0,str.length()-1);

    if(org.compare(str))
        return true;
    return false;
    
}

int main(){

    string s ="aabbaaa";

    cout<<isPalindrome(s);

    return 0;
}
