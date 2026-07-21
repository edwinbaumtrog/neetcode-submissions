class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)):
            j = i + 1
            while j < len(intervals):
                if intervals[i][0] < intervals[j][0]:
                    if intervals[i][1] < intervals[j][0]:
                        j += 1
                        continue
                    left = intervals[i][0]
                    if intervals[i][1] < intervals[j][1]:
                        intervals[i][1] = intervals[j][1]
                        intervals.pop(j)
                    else:
                        intervals.pop(j)
                else:
                    if intervals[i][1] < intervals[j][1]:
                        intervals.pop(i)
                    else:
                        intervals.pop(j)
        return intervals