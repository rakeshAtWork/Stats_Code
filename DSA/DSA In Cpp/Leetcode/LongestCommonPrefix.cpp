#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        string ans = "";
        int count = 0;
        bool flag = true;

        for (int i = 0; i < strs[0].size(); i++) {

            char ch = strs[0][i];

            for (int j = 0; j < strs.size(); j++) {
                if (ch != strs[j][i]) {
                    flag = false;
                }
            }

            if (flag) {
                count++;
            } else {
                break;
            }
        }

        return strs[0].substr(0, count);
    }
};

int main(){
    Solution s1;
    vector<string> s;
    s.push_back("flight");
    s.push_back("flower");
    s.push_back("flow");
    string solution=s1.longestCommonPrefix(s);
    cout<<"The answ is: "<<solution<<endl;
    return 0;
}