class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pr = strs[0]
        for i in range(len(strs)):
            while not(strs[i].startswith(pr)):
                pr = pr[:len(pr)-1]
        return pr