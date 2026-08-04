class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for let in s:
            if let not in dicS:
                dicS[let] = 1
            else:
                dicS[let]+=1
        for let in t:
            if let not in dicT:
                dicT[let] = 1
            else:
                dicT[let]+=1
        if len(dicS)!=len(dicT):
            return False
        for let in dicS:
            
            if let not in dicT or dicS[let]!=dicT[let]:
                return False
            
        return True