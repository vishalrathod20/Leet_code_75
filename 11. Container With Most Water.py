class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0  # Pointer for the left edge
        right = len(height) - 1  # Pointer for the right edge
        max_area = 0  # Variable to store the maximum area

        while left < right:
            width = right - left  # Calculate the width between the two pointers
            height_min = min(height[left], height[right])  # Get the minimum height of the two lines
            area = width * height_min  # Calculate the area

            max_area = max(max_area, area)  # Update max_area if the current area is larger

            # Move the pointer pointing to the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area  # Return the maximum area found
