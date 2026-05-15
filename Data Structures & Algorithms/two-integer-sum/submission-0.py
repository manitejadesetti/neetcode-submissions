class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for index, num in enumerate(nums):
            if num in target_dict:
                return [target_dict[num], index]
            diff = target - num
            target_dict[diff] = index
            
        