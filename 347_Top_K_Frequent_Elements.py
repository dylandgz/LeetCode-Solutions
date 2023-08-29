'''
Time Complexity: O(n)
Space Complexity: O(n)

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #it is returning each key(n is the count number) value(c for the values that have that count) pair
        for n, c in count.items():
            freq[c].append(n)
        print(count)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)
