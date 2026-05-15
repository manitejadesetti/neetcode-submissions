class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        max = 0
        res = s[0]
        while i < n:
            j = i + 1
            while j < n:
                text = s[i:j+1]
                flag = True
                for k in range(len(text)//2):
                    if text[k] != text[len(text)-k-1]:
                        flag = False
                if flag and max < len(text):
                    max = len(text)
                    res = text
                j += 1
            i += 1
        return res
            
        