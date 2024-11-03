class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # Pointer to place non-zero elements
        
        # Iterate through the list
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element with the element at the left pointer
                nums[left], nums[i] = nums[i], nums[left]
                left += 1  # Move the left pointer to the right
        
        # No return statement is needed since we modify nums in-place
