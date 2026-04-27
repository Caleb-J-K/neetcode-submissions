class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = 0 - len(nums)
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] == nums[k]:
                    repeats = repeats + 1
        if repeats > 0:
            return True
        else:
            return False