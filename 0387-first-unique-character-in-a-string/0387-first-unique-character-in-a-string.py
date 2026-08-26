class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = 1+freq.get(i,0)
        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx
        return -1 