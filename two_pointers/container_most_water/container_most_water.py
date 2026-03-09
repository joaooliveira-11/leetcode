class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2 = 0, len(height) - 1

        max_area = -1

        while(p2 > p1):
            curr_area = (p2-p1) * min(height[p1], height[p2])
            max_area = max(curr_area, max_area)

            if height[p1] > height[p2]:
                p2 -=1
            else:
                p1 += 1

        return max_area