class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}

        # Count occurrences of each number
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        # Convert occurrences to a set to check uniqueness
        freq_set = set(count_map.values())
        
        return len(freq_set) == len(count_map)
