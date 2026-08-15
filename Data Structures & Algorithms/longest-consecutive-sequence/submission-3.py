class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_n = 0
        for num in nums:

            if num - 1 not in nums_set:
                count = 0
                num_seq = num
                while num_seq  in nums_set:
                    count += 1
                    num_seq += 1
                max_n = max(max_n, count)
        return max_n


        