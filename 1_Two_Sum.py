'''
Time Complexity: O(n)
Space Complexity: O(n)
'''



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_map ={}
        for i in range(len(nums)):
            if target - nums[i] in h_map:
                return[h_map[target -nums[i]] ,i]
            else:
                h_map[nums[i]] = i
