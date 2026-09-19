import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-each for each in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            heavy_stone = heapq.heappop(stones)
            light_stone  = heapq.heappop(stones)

            if abs(heavy_stone) > abs(light_stone):
                heapq.heappush(stones, -(abs(heavy_stone) - abs(light_stone)))
            print(stones)
        return -stones[0] if len(stones) > 0 else 0