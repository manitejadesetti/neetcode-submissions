class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_sum = [1] * len(nums)
        postfix_sum = [1] * len(nums)
        pre_res = 1
        post_res = 1
        for i in range(1, len(nums)):
            pre_res *= nums[i - 1]
            prefix_sum[i] = pre_res
        for i in range(len(nums) - 2, -1, -1):
            post_res *= nums[i + 1]
            postfix_sum[i] = post_res
        for i in range(len(nums)):
            output.append(prefix_sum[i] * postfix_sum[i])
        
        return output

        