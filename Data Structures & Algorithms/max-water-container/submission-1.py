class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx=0
        i =0
        j = len(heights)-1
        while i< j:
            width= j-i
            h = min(heights[i],heights[j])
            area = width*h
            maxx=max(maxx,area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxx
        