#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int romanToInt(string s) {
        map<char,int> mp;
        mp.insert({'I',1});
        mp.insert({'V',5});
        mp.insert({'X',10});
        mp.insert({'L',50});
        mp.insert({'C',100});
        mp.insert({'D',500});
        mp.insert({'M',1000});

        long ans=0;

        for (int i=0;i<s.size();i++){
            if(s[i]=='I' && s[i+1] == 'V'){
                ans +=4;
                i++;
            }else if(s[i]=='I' && s[i+1] == 'X'){
                ans += 9;
                i++;
            }else if(s[i]=='X' && s[i+1] == 'L'){
                ans += 40;
                i++;
            }else if(s[i]=='X' && s[i+1] == 'C'){
                ans += 90;
                i++;
            }else if(s[i]=='C' && s[i+1] == 'D'){
                ans += 400;
                i++;
            }else if(s[i]=='C' && s[i+1] == 'M'){
                ans += 900;
                i++;
            }else{
                ans += mp[s[i]];
            }
        }


        return ans;
        

    }
};

int main(){
    Solution s1;
    int ans = s1.romanToInt("XC");
    cout<<"The output is : "<<ans<<endl;
    return 0;
}