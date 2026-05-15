class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        i = 0
        str_length = len(s)
        while i < str_length/2:
            if s[i] != s[str_length-i-1]:
                return False
            i += 1
        return True