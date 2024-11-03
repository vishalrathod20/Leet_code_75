class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Reverse the entire string
        s = s[::-1]
        n = len(s)
        
        # Initialize pointers and list to build the result
        left = 0
        right = 0
        result = []
        
        i = 0
        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            
            # Check if we reached the end
            if i == n:
                break
            
            # Start of a new word
            left = right
            
            # Copy the current word to result
            while i < n and s[i] != ' ':
                result.append(s[i])
                i += 1
                right += 1
            
            # Reverse the word just added to result
            result[left:right] = result[left:right][::-1]
            
            # Add a space after the word
            result.append(' ')
            right += 1
            i += 1
        
        # Remove the trailing space and join list into a string
        return ''.join(result).rstrip()
