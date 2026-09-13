class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            d[n]+=1
        for key, v in d.items():
            freq[v].append(key)
        out = []
        for l in freq[::-1]:
            for n in l:
                if len(out)!=k:
                    out.append(n)
                else:
                    break
            if len(out)==k:
                break
        return out