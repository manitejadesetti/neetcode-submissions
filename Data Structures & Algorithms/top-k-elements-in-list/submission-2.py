from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        num_freq = [[] for i in range((len(nums)+1))]
        for num, freq in num_count.items():
            num_freq[freq].append(num)
        output = []
        for i in range(len(num_freq)-1, -1, -1):

            for each in num_freq[i]:
                output.append(each)

                if len(output) == k:
                    return output


        