class Solution:
    def fact(self, n:int) -> int:
        if n > 2:
            return n*self.fact(n-1)
        else:
            return n

    def climbStairs(self, n: int) -> int:
        count = 0
        num_twos = 0
        # n is always the number of ones
        while n > 0:
        # then turn every pair of 1's into 2
            if n - 2 > 0:
                n-=2
                num_twos+=1
                perm = self.fact(n+num_twos)/(self.fact(n)*self.fact(num_twos))
                count+=int(perm)
            else:
                count+=n
                n=0
        # then calculate the number of permutations of the number of 1's with the number of 2's
        # sum it all up
        return count