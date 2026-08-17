class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # make a hash map, and if the matching number is in the map, return the
        # pair, otherwise keep searching until the end. This avoids n squared time
        # and is instead n time

        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        hash_map = {num: index for index, num in enumerate(nums)}

        for i in range(len(nums)):
            match = target - nums[i]
            if match in hash_map and nums.index(match) != i:
                match_index = nums.index(match)
                if i < match_index:
                    return [i, match_index]
                else:
                    return [match_index, i]
        