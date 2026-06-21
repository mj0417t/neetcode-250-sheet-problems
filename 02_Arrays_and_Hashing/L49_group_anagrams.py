from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # res=defaultdict(list)
        # for s in strs:
        #     sorted_s=''.join(sorted(s))
        #     res[sorted_s].append(s)
        # return list(res.values())
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())