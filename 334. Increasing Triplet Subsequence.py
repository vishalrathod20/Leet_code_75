

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                # Update first if num is smaller than or equal to the current first
                first = num
            elif num <= second:
                # Update second if num is greater than first but smaller than or equal to second
                second = num
            else:
                # If we find a num greater than both first and second, return True
                return True
        
        # If no such triplet is found, return False
        return False
