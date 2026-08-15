class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for each in range(1, n):
            pref[each] = pref[each - 1] * nums[each - 1]
        for each in range(n - 2, -1, -1):
            suff[each] = suff[each + 1] * nums[each + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

        