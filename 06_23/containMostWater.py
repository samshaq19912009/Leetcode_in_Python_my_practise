class Solution:
    def maxArea(self, height):
        n = len(height)
        L, R = 0, n-1
        if L >= R:
            return 0
        
        area = 0

        while L < R:
            tmp = (R-L)*min(height[R], height[L])

            area = max(area, tmp)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
                
        return area
