# Working code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We have an assortded array so we can use binary search

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1