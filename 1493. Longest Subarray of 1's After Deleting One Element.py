from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize pointers and counters
        left = 0           # Left pointer for sliding window
        max_len = 0        # To keep track of the maximum length of 1's subarray after deleting one element
        zero_count = 0     # To count the number of zeros in the current window

        # Iterate with the right pointer over each element in the array
        for right in range(len(nums)):
            # If current element is 0, increment zero_count
            if nums[right] == 0:
                zero_count += 1
            
            # If there are more than one zero in the current window, adjust the left pointer
            while zero_count > 1:
                # If the element at the left pointer is 0, decrement zero_count as it will be removed from the window
                if nums[left] == 0:
                    zero_count -= 1
                # Move the left pointer to shrink the window
                left += 1
            
            # Calculate the length of the current window and update max_len
            # (right - left) gives the size of the window with at most one 0
            max_len = max(max_len, right - left)
        
        return max_len  # Return the maximum length found
