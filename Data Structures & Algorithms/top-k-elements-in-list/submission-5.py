class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in nums]
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        for key in freq_dict:
            freq_list[freq_dict[key] - 1].append(key)
        
        res = []
        for each_list in range(len(freq_list) - 1, -1, -1):
            for each in freq_list[each_list]:
                print(len(res))
                if len(res) == k:
                    return res
                res.append(each)
        return res

