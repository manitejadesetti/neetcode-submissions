class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = 0
        nums_length = 0
        for each in nums:
            nums_sum += each
            
            nums_length += 1
        sum_formula = (nums_length * (nums_length + 1)) // 2 
        return sum_formula - nums_sum
        