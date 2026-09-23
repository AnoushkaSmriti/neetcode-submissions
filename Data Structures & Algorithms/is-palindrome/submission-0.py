class Solution:
    def isPalindrome(self, s: str) -> bool:
    # 1. Clean the original string first
        newstr = ''
        for c in s:
            if c.isalnum():
                # newstr.join(c.lower())
                newstr += c.lower()

    
    
    # 2. Compare them
        return newstr == newstr[::-1]

        