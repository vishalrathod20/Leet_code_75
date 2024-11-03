class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for string s
        for j in range(len(t)):
            # If there's a character match, move the pointer for s
            if i < len(s) and s[i] == t[j]:
                i += 1
        
        # If we've matched all characters of s, return True
        return i == len(s) 
