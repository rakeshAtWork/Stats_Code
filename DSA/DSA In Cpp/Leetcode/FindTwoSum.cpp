#include<bits/stdc++.h>
#include "../../../../../../../../MinGW/lib/gcc/mingw32/6.3.0/include/c++/bits/gslice.h"
using namespace std;
int main(){
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size() ; j++) {
                if(nums[j]+nums[i] == target){
                    ans.push_back(i);
                    ans.push_back(j);
                    //break;
                }
            }
        }
        return ans;
    }
};

}
