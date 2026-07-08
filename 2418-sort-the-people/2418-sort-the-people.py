class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for j in range(len(names)-1):
            for i in range(len(names)-j-1):
                if heights[i]<heights[i+1]:
                    heights[i] , heights[i+1] =  heights[i+1] , heights[i]
                    names[i] , names[i+1] = names[i+1] , names[i]
        return names
            
            
        