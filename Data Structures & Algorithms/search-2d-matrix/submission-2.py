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

            top, bot = 0, len(matrix) - 1

            while top <= bot:
                row = (top + bot) // 2

                if matrix[row][0] > target:
                    bot = row - 1
                elif matrix[row][-1] < target:
                    top = row + 1
                else:
                    break

            if top > bot:
                return False
            l, h = 0, len(matrix[row])
            return self.binary_search(l, h, matrix[row], target)
                