class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_product = 1
        res = []
        count = 0
        for num in nums:
            if num:
                product *= num
            else:
                count += 1
            zero_product *= num
        for num in nums:
            if num:
                res.append(int(zero_product/num))
            elif count > 1:
                res.append(0)
            else:
                res.append(product)
        return res