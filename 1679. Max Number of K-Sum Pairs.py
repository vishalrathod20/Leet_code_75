class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = len(nums)-1

        nums.sort()

        while left < right:
            sum = nums[left] + nums[right]

            if sum == k:
                count+=1
                left+=1
                right-=1
            elif sum > k:
                right-=1
            elif sum < k:
                left+=1
        
        return count
