class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        reach = []

        for car in cars:
            reach.append((target - car[0])/car[1])

        i = len(reach) - 1

        while i > 0:
            if reach[i - 1] <= reach[i]:
                reach.pop(i - 1)
            i -= 1

        return len(reach)
        
        