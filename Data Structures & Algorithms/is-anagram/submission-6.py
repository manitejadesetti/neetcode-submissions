from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)
        for char in s:
            countS[char] += 1
        for char in t:
            countT[char] += 1
        print(countS)
        print(countT)
        return countS == countT

        