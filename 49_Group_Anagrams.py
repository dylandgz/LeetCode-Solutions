
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dictionary that will store arrays of anagrams
        # create lists that will represent keys of anagrams
        # important to use defaultdict because it helps deal with key error
        # note the use of ord()
        answe r =defaultdict(list)

        for word in strs:
            coun t =[0 ] *26
            for s in word:
                count[ord ('a' ) -ord(s) ]+ =1

            answer[tuple(count)].append(word)
        return answer.values()