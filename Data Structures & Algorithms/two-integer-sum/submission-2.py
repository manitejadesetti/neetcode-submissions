class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in target_dict:
                return [target_dict[diff], index]
            target_dict[num] = index
        
        