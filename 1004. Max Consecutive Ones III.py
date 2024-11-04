class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # If we encounter a 0, increase the zero_count
            if nums[right] == 0:
                zero_count += 1

            # If zero_count exceeds k, move the left pointer to shrink the window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update max_length with the size of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length
