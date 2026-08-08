from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if '0' in str(n):
            return n
        while True:
            r = prod(int(d) for d in str(n))
            if r%t == 0:
                return n
            n += 1