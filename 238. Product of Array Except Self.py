class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n  # Initialize the result array with 1s
        
        # Calculate prefix products and store in ans
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        
        # Calculate postfix products and multiply with the prefix product in ans
        postfix = 1
        for j in range(n - 1, -1, -1):
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans
