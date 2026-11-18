class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        total = 0
        if len(stones) == 0:
            return total

        while 1 <len(stones):
            stones = sorted(stones,reverse=True)
            stones[0] -=stones[1]
            stones.remove(stones[1])

        return stones[0]
        
                