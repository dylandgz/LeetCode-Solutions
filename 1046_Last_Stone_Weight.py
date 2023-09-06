
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: x=0
        y=0
        while len(stones)>1:
            stones=sorted(s t ones)
            print(len(stones))
            y=stones[- 1 ]
            x=stones[- 2 ]
            diff=y-x
            stones.pop()
            stones.pop()
            if diff!=0:
                stones.append(diff)
        if len(stones)==1:
            return stones[0]
        else:
            return 0