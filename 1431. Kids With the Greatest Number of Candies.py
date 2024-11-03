class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         # Find the maximum number of candies in the list
        maxCandies = max(candies)
        
        # For each child, check if adding extraCandies gives them at least maxCandies
        result = [(candy + extraCandies >= maxCandies) for candy in candies]
        
        return result
