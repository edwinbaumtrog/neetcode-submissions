from typing import List
import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = np.array(nums)
        uniques, counts = np.unique(arr, return_counts=True)

        indices = np.argsort(counts)[::-1][:k]
        frequent_values = uniques[indices]

        return frequent_values.tolist()