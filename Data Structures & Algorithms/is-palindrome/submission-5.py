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
       s  = s.lower()
       l = 0
       r = len(s)-1

       while l<r:
            # while l<r and not self.isAlphanum(s[l]):
            if not s[l].isalnum():
               l+=1
               continue
            # while r>l and not self.isAlphanum(s[r]):
            if not s[r].isalnum():
               r-=1
               continue

            if s[l]!=s[r]:
               return False

            l+=1
            r-=1
       return True
    


        



        