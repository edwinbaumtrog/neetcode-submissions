import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [cnt for cnt in count.values()]
        heapq.heapify_max(heap)
        time = 0
        queue = deque()
        while heap or queue:
            while queue:
                if queue[0][1] < time:
                    heapq.heappush_max(heap,queue.popleft()[0])
                else:
                    break
            if heap:
                count_task = heapq.heappop_max(heap) - 1
                if count_task > 0:
                    queue.append((count_task, time + n))
            time += 1
        return time