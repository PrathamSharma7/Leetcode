class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_nums = set(nums)
        i = 1
        while True:
            if i*k not in set_nums:
                return i*k
            else:
                i+=1