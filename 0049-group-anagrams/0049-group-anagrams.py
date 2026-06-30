from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            lis = [0] * 26
            for j in i:
                lis[ord(j) - ord("a")] += 1 

            d[tuple(lis)].append(i)
            

        A = list(d.values())
        return A[::-1]
        

        

