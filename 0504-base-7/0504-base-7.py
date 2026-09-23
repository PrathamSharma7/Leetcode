class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        snum = str(num)
        result = ""
        num = abs(num)
        while num:
            result+=str(num%7)
            num//=7
        if snum.startswith('-'):
            result+='-'
        return result[::-1]