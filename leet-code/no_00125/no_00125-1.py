class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert into lowercase letters
        s = s.lower()
        
       # Only alphabet and numeric characters are not removed
        s = re.sub('[^a-z0-9]', '', s)

        # Check the palindrome
        return s[::] == s[::-1]