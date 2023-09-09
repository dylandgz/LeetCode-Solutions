

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # assuming that the majority elements always exists in the array
        # We can use a hashtable to store the number of times the number is in the list.
        # We then need to iterate through the hashtable and return the largest value

        table = {}

        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
        print(table)

        max = 0
        max_key = 0
        for key in table:
            if max < table[key]:
                max = table[key]
                max_key = key

        return max_key