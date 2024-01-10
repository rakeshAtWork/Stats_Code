# include<iostream>
using namespace std;

int main(){

    string s = "Rakesh";

    int len = s.size();

    s[len-1]='x';   // here we can say that string is mutable i.e we can change or alter the value.

    cout<<s<<endl;


    return 0;
}