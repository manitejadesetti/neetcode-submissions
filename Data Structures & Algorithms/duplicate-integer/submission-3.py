class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_set = set()
        for num in nums:
            if num in count_set:
                return True
            count_set.add(num)
        return False

        

        