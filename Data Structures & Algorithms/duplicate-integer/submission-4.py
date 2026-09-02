class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if x in d:
                return True
            d[x] = True
        return False
