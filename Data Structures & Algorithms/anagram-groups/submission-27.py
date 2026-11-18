class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for st in strs:
            temp = ''.join(sorted(st))
            if temp not in anagrams.keys():
                anagrams[temp] = [st]
            else:
                anagrams[temp].append(st)
        return list(anagrams.values())