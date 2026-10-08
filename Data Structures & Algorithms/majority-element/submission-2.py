class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_max = nums[0]
        frequency = 0
        for value in nums:
            if current_max == value:
                frequency += 1
            else:
                frequency -= 1
            if frequency == 0:
                current_max = value
                frequency += 1
        return current_max
        