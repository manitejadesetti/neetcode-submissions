class Solution:

    def binary_search(self, start, end, nums, target):
        mid = (start + end) // 2


        if nums[mid] == target:
            return mid

        if end < start:
            return -1
        
        if nums[mid] > target:
            return self.binary_search(start, mid - 1, nums, target)
        else:
            return self.binary_search(mid + 1, end, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        

        index = self.binary_search(l, h, nums, target)

        return index

        
            


        