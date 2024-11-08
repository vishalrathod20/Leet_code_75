from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False 
        if set(word1) != set(word2):
            return False
        
        frq1 = Counter(word1)
        frq2 = Counter(word2)

        return sorted(frq1.values()) == sorted(frq2.values())
