class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            hold = [0] * 26
            for c in s:
                hold[ord(c)-ord("a")]+=1
            out[tuple(hold)].append(s)
        return list(out.values())
            