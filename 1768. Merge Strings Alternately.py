class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = [] 

        minLength = min(len(word1),len(word2))

        for i in range(minLength):
            merged.append(word1[i])
            merged.append(word2[i])
        
        merged.append(word1[minLength:])
        merged.append(word2[minLength:])

        return ''.join(merged)
