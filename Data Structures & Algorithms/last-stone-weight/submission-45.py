class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while 1 <len(stones):
            stones = sorted(stones,reverse=True)
            stones[0] -=stones[1]
            stones.remove(stones[1])

        return stones[0]
        
                