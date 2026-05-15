class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       res = {}
       for index, each in enumerate(nums):
            diff = target-each
            if each in res:
                return [res[each], index]
            res[diff] = index

        