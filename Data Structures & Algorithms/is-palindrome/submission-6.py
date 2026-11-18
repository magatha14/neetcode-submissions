class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''.join(c for c in s if c.isalnum()).lower()
        print(alnum)
        l = len(alnum)
        if l < 2: return True
        first = ''.join(alnum[:math.floor(l/2)])
        second = ''.join(reversed(alnum[math.ceil(l/2):]))
        print("first: ", first)
        print("second: ", second)
        return first == second
