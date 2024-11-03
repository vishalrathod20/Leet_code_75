class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ansIndex = 0
        n = len(chars)

        while i < n:
            j = i + 1
            # Find the end of the current character sequence
            while j < n and chars[i] == chars[j]:
                j += 1
            
            # Store the current character
            chars[ansIndex] = chars[i]
            ansIndex += 1
            
            count = j - i  # Count the occurrences of the character
            if count > 1:
                # Convert the count to string and store each character
                for c in str(count):
                    chars[ansIndex] = c
                    ansIndex += 1
            
            # Move to the next new character
            i = j
        
        return ansIndex  # Return the new length of the compressed list
