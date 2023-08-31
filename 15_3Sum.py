

#need to review
#Code is not passing all the tests
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # cannot think of an optimal solution so I will start with brute force
        answer = []
        combination = []

        nums = sorted(nums)
        print(nums)

        l = 0
        m = l + 1
        r = len(nums) - 1

        while l < r or l != r:
            sum = nums[l] + nums[m] + nums[r]
            if m > r or m == r or l == m or l == r:
                old = l
                l += 1
                for index in range(l, len(nums)):
                    if nums[old] != nums[index]:
                        l = index
                        break
                m = l + 1
                r = len(nums) - 1
            elif sum == 0:
                print(f"values l={l}, m={m},r={r}")
                combination = [nums[l], nums[m], nums[r]]
                answer.append(combination)
                m += 1
                combination = []

            elif sum > 0:
                r -= 1

            elif sum < 0:
                m += 1

        return answer
