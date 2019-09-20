class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        most_water = 0
        while left < right:
            times = right - left
            if height[left] < height[right]:
                current = height[left]* times
                left+=1
            else:
                current = height[right]* times
                right-=1
            most_water=max(most_water,current)
        return most_water
