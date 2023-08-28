'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
#May need optimization

class Solution:
    def containsDuplicate(self, nums):
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False


