class Solution:
    def binary_search(self, start, end, nums, target):
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

            for each in matrix:

                if each[0] <= target and each[-1] >= target:
                    return self.binary_search(0, len(each) - 1, each, target)
            return False
