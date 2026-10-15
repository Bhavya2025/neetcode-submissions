class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        output = []
        for i in nums:
            if (hash_map.get(i) is None):
                hash_map[i] = 1
            else:
                hash_map[i] = hash_map[i] + 1
        frequency_map = {}
        for key, value in hash_map.items():
            if (frequency_map.get(value) is None):
                frequency_map[value] = [key]
            else:
                frequency_map[value].append(key)
        for frequency in range(len(nums), 0, -1):
            if frequency in frequency_map:
                for number in frequency_map[frequency]:
                    output.append(number)
                if len(output) == k:
                    return output
            
            