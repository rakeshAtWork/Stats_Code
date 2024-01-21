#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        multiset<int> mt;

        for(int i=0;i<nums.size();i++){
            mt.insert(nums[i]);
        }

        mt.erase(val);
        

        auto it = mt.begin();

        for(int i=0;i<mt.size();i++){
            nums[i]=*it;
            it++;
        }

        return mt.size();



    }
};
int main(){
    vector<int> v;
    v.push_back(0);
     v.push_back(1);
 v.push_back(2);
      v.push_back(2);
      v.push_back(3);
       v.push_back(0);
        v.push_back(4);
         v.push_back(2);
    Solution s;
  int ans= s.removeElement(v,2);

  cout<<ans<<endl;

  for(int i=0;i<v.size();i++){
    cout<<v[i]<<" ";
  }

    return 0;
}