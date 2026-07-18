class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            if len(heap) < k:
                heap.append(point)
            elif len(heap) == k:
                point_val = math.sqrt((point[0])**2 + (point[1])**2)
                for i, stored in enumerate(heap):
                    stored_val = math.sqrt((stored[0])**2 + (stored[1])**2)
                    if point_val < stored_val:
                        heap[i] = point
                        point = stored
                        point_val = stored_val
        return heap