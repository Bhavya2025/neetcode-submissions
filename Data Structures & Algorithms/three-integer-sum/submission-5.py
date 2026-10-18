class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        output = set()
        for i in range(size - 2):
            start = i + 1
            end = size - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    output.add((nums[i],nums[start],nums[end]))
                    start += 1
                    end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return list(output)