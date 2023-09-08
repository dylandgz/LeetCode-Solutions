# My updated solution using the code template

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We have an assortded array so we can use binary search

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if target <= nums[m]:
                r = m
            else:
                l = m + 1

        if nums[l] == target:
            return l

        return -1
