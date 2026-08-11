class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_ends = -1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                prefix_ends = i-1
                break
        if prefix_ends == -1:
            only_prefix_array = nums
        else:
            only_prefix_array = nums[:prefix_ends+1]
        s = sum(only_prefix_array)
        while True:
            if s not in nums:
                return s
            s+=1