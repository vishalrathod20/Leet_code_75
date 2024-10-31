class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,1);
        int prefix = 1;
        int postfix = 1;
        for(int i = 0; i<n; i++){
            ans[i] = prefix;
            prefix *= nums[i];
        }

        for(int j = n-1; j>=0; j--){
            ans[j] *= postfix;
            postfix *= nums[j];
        }
        return ans;
    }
};
