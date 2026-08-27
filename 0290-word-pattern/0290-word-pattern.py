class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(pattern)):
            a = pattern[i]
            b = words[i]

            if a in d1 and d1[a] != b:
                return False

            if b in d2 and d2[b] != a:
                return False

            d1[a] = b
            d2[b] = a

        return True