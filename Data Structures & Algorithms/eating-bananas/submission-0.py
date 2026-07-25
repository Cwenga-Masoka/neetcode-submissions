class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        output = 0

        while l <= r:
            m = l + ((r - l)//2)
            
            totalTime = 0
            
            for pile in piles:
                totalTime += math.ceil(pile/m)
            
            if totalTime <= h:
                output = m
                r = m -1

            else:
                l = m + 1
        
        return output
