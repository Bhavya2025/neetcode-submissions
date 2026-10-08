class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for value in nums:
            if d.get(value) is None:
                d[value] = 1
            else:
                d[value] += 1
            if d[value] > n // 2:
                return value
        