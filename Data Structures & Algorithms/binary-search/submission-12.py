class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            n = l + ((h - l) // 2)
            if nums[n] > target:
                h = n - 1
            elif nums[n] < target:
                l = n + 1
            else:
                return n
        return -1