class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        longest = 0
        output = []
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                maxi = 1
                while num + maxi in nums:
                    maxi += 1
                longest = max(maxi, longest)
        return longest