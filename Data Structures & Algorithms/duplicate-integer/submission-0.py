class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for each in nums:
            if not each in nums_count:
                nums_count[each] = 1
            else:
                nums_count[each] += 1
            if nums_count[each] > 1:
                return True
        return False