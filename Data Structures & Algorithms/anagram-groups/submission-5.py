class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list[str])
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c)-97]+=1
            d[tuple(counter)].append(s)

        return list(d.values())