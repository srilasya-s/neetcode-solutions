class Solution:
    def maxArea(self, heights: List[int]) -> int:
       res=0
       l=0
       r=len(heights)-1
        
       while l < r:
          p1 = heights[l]
          p2 = heights[r]
          Area = min(p1,p2) * (r - l)
          res=max(res, Area)
          if p1 <= p2:
             l += 1
          else:
             r -= 1
       return res
