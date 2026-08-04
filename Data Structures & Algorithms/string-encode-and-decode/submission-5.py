class Solution:

    def encode(self, strs: List[str]) -> str:
        out =""
        for s in strs:
            out += str(len(s)) + "\\" + s
            
        return out
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        out = []
        
        while i < len(s):
            if s[j]=="\\" and s[j-1].isnumeric():
                lenWord = int(s[i:j])
                out.append(s[j+1: j+lenWord+1])
                i = j + lenWord + 1
                
                
            j+=1
        return out