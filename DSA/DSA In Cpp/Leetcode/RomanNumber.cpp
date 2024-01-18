#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
        map<char,int> mp;
        mp.insert({'I',1});
        mp.insert({'V',5});
        mp.insert({'X',10});
        mp.insert({'L',50});
        mp.insert({'C',100});
        mp.insert({'D',500});
        mp.insert({'M',1000});

        int ans=0;

        for (auto it :s){
            cout<<it<<endl;
        }

    }


int main(){



    return 0;
}

