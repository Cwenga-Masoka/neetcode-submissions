class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i]>heights[j]:
                    if (heights[j]*(j-i))>maximum:
                        maximum = heights[j]*(j-i)
                
                elif heights[i]<heights[j]:
                    if (heights[i]*(j-i))>maximum:
                        maximum = heights[i]*(j-i)
                
                elif heights[j]==heights[i]:
                    if (heights[i]*(j-i))>maximum:
                        maximum = heights[j]*(j-i)

        return maximum