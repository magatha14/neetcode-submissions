class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        total = 0
        if len(stones) == 0:
            return total
        if len(stones) == 1:
            return stones[0]

        i = 0
        j = 1
        while j <len(stones):
            stones = sorted(stones,reverse=True)
            stones[0] -=stones[1]
            stones.remove(stones[1])

        return stones[0]
        
                