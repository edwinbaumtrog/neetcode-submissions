class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = self.heaping(stones)

        while len(heap) > 1:
            y = self.pop(heap)
            x = self.pop(heap)

            if x < y:
                self.push(heap, y - x)

        if heap:
            return heap[0]

        return 0

    def sift_down(self, heap: List[int], i: int) -> None:
        n = len(heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and heap[left] > heap[largest]:
                largest = left

            if right < n and heap[right] > heap[largest]:
                largest = right

            if largest == i:
                break

            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest

    def heaping(self, heap: List[int]) -> List[int]:
        last_parent = len(heap) // 2 - 1

        for i in range(last_parent, -1, -1):
            self.sift_down(heap, i)

        return heap

    def pop(self, heap: List[int]) -> int:
        maximum = heap[0]
        last = heap.pop()

        if heap:
            heap[0] = last
            self.sift_down(heap, 0)

        return maximum

    def push(self, heap: List[int], val: int) -> None:
        heap.append(val)
        i = len(heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if heap[parent] >= heap[i]:
                break

            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent