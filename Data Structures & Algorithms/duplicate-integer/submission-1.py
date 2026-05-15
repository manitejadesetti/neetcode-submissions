class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for each in nums:
            if each in res:
                return True
            res.add(each)
        return False