class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            current_area = min(left_height,right_height) * (right - left)
            if current_area > max_area: max_area = current_area

            if left_height == right_height:
                left += 1
                right -= 1
            elif left_height > right_height:
                right -= 1
            else:
                left += 1
        return max_area