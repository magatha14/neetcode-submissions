class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count.keys():
                count[n] = 1
            else:
                count[n]+=1
        count = dict(sorted(count.items(), key = lambda item: item[1], reverse=True))
        return list(count.keys())[:k]
        