class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # hashSet = {}

        # for i in nums:
        #     if i not in hashSet:
        #         hashSet[i] = 1
        #     else:
        #         hashSet[i] += 1

        # for i in hashSet:
        #     if hashSet[i] == 1:
        #         return i

        term = 0
        for i in nums:
            term = term ^ i
        return term
        