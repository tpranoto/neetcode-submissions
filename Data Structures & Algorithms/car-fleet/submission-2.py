class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []
        for i in range(len(position)):
            position_speed.append((position[i],speed[i]))
        
        position_speed.sort(reverse=True)

        stack = []
        for pos, spe in position_speed:
            eta = (target - pos) / spe
            print(eta)
            if len(stack) == 0:
                stack.append(eta)
                continue
            
            if stack[-1] < eta:
                stack.append(eta)
        
        return len(stack)
            