class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0
        
        while i < length and n > 0:
            if flowerbed[i] == 1:
                # If there's a flower at the current position, skip the next plot
                i += 2
            elif i == length - 1 or flowerbed[i + 1] == 0:
                # Plant a flower if at the last plot or if the next plot is empty
                n -= 1
                i += 2  # Move two positions forward since we just planted
            else:
                # If the next plot is occupied, skip to the next possible empty spot
                i += 3
        
        # Return True if we managed to plant all n flowers, otherwise False
        return n <= 0
