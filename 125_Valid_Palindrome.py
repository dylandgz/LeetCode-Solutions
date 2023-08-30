'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:

    def isPalindrome(self, s: str) -> bool:
        # convert all letters into lowercase and remove all non-alphanumeric characters

        s = s.lower()
        new_s = ""
        # new string should only be name of alphanumeric characters
        for i in s:
            if i.isalnum():
                new_s += i

        print(new_s)
        # return true only if backwards and forwards are the same
        if new_s == new_s[::-1]:
            return True
        else:
            return False
