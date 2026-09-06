class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x  = nums[i]
            needed = target - x
            if needed in d:
                return [d[needed], i]
            d[x] = i