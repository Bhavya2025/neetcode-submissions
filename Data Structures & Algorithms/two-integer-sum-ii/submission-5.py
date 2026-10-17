class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            mid = numbers[start] + numbers[end]
            if mid == target:
                return [start + 1, end + 1]
            elif mid > target:
                end -= 1
            else:
                start += 1