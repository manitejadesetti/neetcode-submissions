class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre_res = 1
        post_res = 1
        for i in range(len(nums)):
            
            output[i] *= pre_res
            pre_res *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post_res
            post_res *= nums[i]
        
        
        return output

        