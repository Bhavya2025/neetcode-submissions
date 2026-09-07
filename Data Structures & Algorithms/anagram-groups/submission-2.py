class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord('a')] += 1
            key = tuple(a)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        values = []
        for key, value in d.items():
            values.append(value)
        return values