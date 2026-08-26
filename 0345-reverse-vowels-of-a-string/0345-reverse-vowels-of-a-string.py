class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        ov = ""
        for i in range(len(s)):
            if s[i] in vowels:
                ov += s[i]
                s = s[:i] + '+' + s[i+1:]
        ov = ov[::-1]
        for i in range(len(s)):
            if s[i] == '+':
                s = s[:i] + ov[0] + s[i+1:]
                ov = ov[1:]
        return s