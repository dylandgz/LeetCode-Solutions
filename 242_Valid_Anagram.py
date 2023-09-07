class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they are not the same size then they are not anagrams
        # need hash table to store letters for both words
        # compare the tables and if true then yes it is an anagram

        hash_s = {}
        hash_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in hash_s:
                hash_s[i] = 1
            else:
                hash_s[i] += 1

        for k in t:
            if k not in hash_t:
                hash_t[k] = 1
            else:
                hash_t[k] += 1

        for y in hash_s:
            if hash_s[y] != hash_t.get(y, 0):
                return False

        return True
