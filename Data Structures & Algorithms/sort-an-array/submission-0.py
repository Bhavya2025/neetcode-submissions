class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if (length <= 1): return nums
        left_len = length // 2 
        right_len = length - left_len
        
        left = nums[0:left_len]
        right = nums[left_len:length]

        left = self.sortArray(left)
        right = self.sortArray(right)
        return self.merge(left, right)

    def merge (self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        i = 0
        j = 0
        arr = []
        while (i < len1 or j < len2):
            if i == len1:
                arr.append(list2[j])
                j += 1
            elif (j == len2 or list1[i] < list2[j]):
                arr.append(list1[i])
                i += 1 
            else :
                arr.append(list2[j])
                j += 1
        return arr