import math
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        res = res * sign
        if res < -math.pow(2, 31) or res > (math.pow(2, 31) - 1):
            return 0
        return res


        