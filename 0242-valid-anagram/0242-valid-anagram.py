class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = {}
        if len(s) != len(t):
            return False
        for i in s:
            f[i] = f.get(i,0) +1
        for j in t:
            if j not in f:
                return False
            f[j] -= 1
        return not any(f.values())