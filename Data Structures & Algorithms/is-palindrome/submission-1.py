class Solution:

    def isAlphanum(self, c):
        return (ord('a')<=ord(c)<=ord('z') or
        ord('A')<=ord(c)<=ord('Z') or
        ord('0')<=ord(c)<=ord('9')
        )

    def isPalindrome(self, s: str) -> bool:
    # # 1. Clean the original string first
    #     newstr = ''
    #     for c in s:
    #         if c.isalnum():
    #             # newstr.join(c.lower())
    #             newstr += c.lower()

    
    
    # # 2. Compare them
    #     return newstr == newstr[::-1]

    #  two pointer approach
       l = 0
       r = len(s)-1

       while l<r:
            while l<r and not self.isAlphanum(s[l]):
               l+=1
            while r>l and not self.isAlphanum(s[r]):
               r-=1

            if s[l].lower()!=s[r].lower():
               return False

            l+=1
            r-=1
       return True
    


        



        