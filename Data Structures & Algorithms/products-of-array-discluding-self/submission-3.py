class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_product = [1]
        suffix_product = [1]
        prefix_res = 1
        suffix_res = 1
        for each in range(0, len(nums) - 1):
            prefix_res *= nums[each]
            prefix_product.append(prefix_res)
        for each in range(len(nums) - 1, 0,  -1):
            suffix_res *= nums[each]
            suffix_product.append(suffix_res)
        for each in range(len(nums)):
            res.append(prefix_product[each] * suffix_product[len(nums) - 1 - each])

        return res


        