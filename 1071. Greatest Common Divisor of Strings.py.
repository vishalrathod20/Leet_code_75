class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 is equal to str2 + str1, which confirms they have a common divisor pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Return the substring from 0 to gcd of the lengths of str1 and str2
        return str1[:gcd(len(str1), len(str2))]
