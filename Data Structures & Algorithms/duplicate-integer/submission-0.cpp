class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> unique_nums;
        for(int num: nums){
            int size_before {unique_nums.size()};
            unique_nums.insert(num);
            int size_after {unique_nums.size()};
            if(size_after - size_before == 0){
                return true;
            }
        }
        return false;
    }
};