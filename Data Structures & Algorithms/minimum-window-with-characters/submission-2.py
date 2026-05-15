from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not len(t):
            return ""
        l = 0
        have, need = 0, len(t)
        min_len = float("infinity")
        res = [-1, -1]
        t_count, s_count = defaultdict(int), defaultdict(int)
        for each in t:
            t_count[each] += 1
        for r in range(len(s)):
            char = s[r]
            s_count[char] += 1
            if char in t_count and s_count[char] <= t_count[char]:
                have += 1
            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] 




        