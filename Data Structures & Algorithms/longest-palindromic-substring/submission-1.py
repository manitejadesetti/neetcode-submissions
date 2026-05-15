class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        max_res = ""
        # s =  'aabbac'
        for i in range(len(s)):
            for j in range(i, len(s)):
                res = s[i:j + 1]
                k = 0
                flag = True
                while k < len(res)/2:
                    if flag and res[k] != res[len(res) - 1 - k]:
                        flag = False
                    k += 1
                if flag and resLen < len(res):
                    max_res = res
                    resLen = len(res)
        return max_res