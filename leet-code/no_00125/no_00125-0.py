class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs : List = []
        
        # Convert into lowercase letters
        s = s.lower()
        
        # Only alphabet and numeric character is appended into list
        for char in s:
            if char.isalnum():
                strs.append(char)
                
        # Check the palindrome
        return strs[::] == strs[::-1]