class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(curr, path, remaining):
            if remaining == 0:
                result.append(list(path))
                return
            for i in range(curr,len(candidates)):
                if candidates[i] > remaining :
                    break
                path.append(candidates[i])
                backtrack(i,path,remaining-candidates[i])
                path.pop()
            
        backtrack(0,[],target)
        return result
