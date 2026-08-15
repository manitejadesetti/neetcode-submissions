from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in sum_dict:
                return [sum_dict[diff], i]
            sum_dict[num] = i
