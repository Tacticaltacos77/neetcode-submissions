class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            try:
                while not s[l].isalnum():
                        l+=1
                while not s[r].isalnum():
                        r-=1
            except:
                pass
            if l>=r:
                return True
            if s[l] == s[r]:
                l+=1
                r-=1  
            else:
                return False
        return True