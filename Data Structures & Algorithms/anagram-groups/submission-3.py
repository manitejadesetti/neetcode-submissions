from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group  = defaultdict(list)
        for word in strs:
            count_tuple = [0] * 26

            for char in word:
                count_tuple[ord(char) - ord('a')] += 1

            anagram_group[tuple(count_tuple)].append(word)
        return list(anagram_group.values())

            
        