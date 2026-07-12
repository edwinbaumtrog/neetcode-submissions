class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            for j in range(i, len(position)):
                if position[i] > position[j]:
                    position[i], position[j] = position[j], position[i]
                    speed[i], speed[j] = speed[j], speed[i]
        reach = []

        for i in range(len(position)):
            reach.append((target - position[i])/speed[i])

        i = len(reach) - 1

        while i > 0:
            if reach[i - 1] <= reach[i]:
                reach.pop(i - 1)
            i -= 1

        return len(reach)
        
        