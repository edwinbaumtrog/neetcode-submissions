import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            one, two = heapq.heappop(heap), heapq.heappop(heap)
            if one < two:
                heapq.heappush(heap, one - two)
        return -1 * heap[0] if heap else 0


        