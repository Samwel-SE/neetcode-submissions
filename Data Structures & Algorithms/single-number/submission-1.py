class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        term = 0
        for i in nums:
            term = term ^ i
        return term
        