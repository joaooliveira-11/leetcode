from typing import List

# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.
def maxArea(heights: List[int]) -> int:
    # naive solution would be to test all pairs with O(n^2)

    p1, p2 = 0, len(heights) - 1

    max_area = -1
    while(p1 != p2):
        curr_area = (p2-p1) * min(heights[p1], heights[p2]) # Area calculation formula
        max_area = max(max_area, curr_area)

        if heights[p1] > heights[p2]:
            p2 -= 1
        else:
            p1 += 1
    
    return max_area