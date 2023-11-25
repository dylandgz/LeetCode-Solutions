class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dont matter what the fist value is
        min_num = nums[0]
        max_num = nums[0]
        num_dict = {}
        for n in nums:
            num_dict[n] = 0
            min_num = min(min_num, n)
            max_num = max(max_num, n)

        counter = 1
        for i in range(min_num, max_num):
            print(i)
            if i + 1 in num_dict:
                counter += 1
            else:
                return counter
        return counter