class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        counts_dict = [[] for i in range(len(nums) + 1)]
        for each in freq_dict:
            counts_dict[freq_dict[each]].append(each)
        
        
        for i in range(len(counts_dict) - 1, 0, -1):
            for j in counts_dict[i]:
                res.append(j)
                if len(res) == k:
                    return res

        