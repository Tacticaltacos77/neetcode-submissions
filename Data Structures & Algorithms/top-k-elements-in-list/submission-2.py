class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        out_nums = sorted(tuple(dic.items()), key=lambda x: x[1])[::-1]
        out = []
        for i in range(k):
            out.append(out_nums[i][0])
        return out