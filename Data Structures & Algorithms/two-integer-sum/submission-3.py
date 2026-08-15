from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in sum_dict:
                return [sum_dict[diff], index]
            sum_dict[num] = index
