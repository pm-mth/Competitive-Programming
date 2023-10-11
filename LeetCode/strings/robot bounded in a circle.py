class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        start = [0, 0]
        instructions
        r = 0
        length = 0
        left, right, north, south = False, False, True, False
        while length <= len(instructions) * 4:
            if r == len(instructions):
                length += len(instructions)
                r = 0
                if tuple(start) == (0,0):
                    return True
            if north:
                if instructions[r] == "G":
                    start[1] += 1
                if instructions[r] == "L":
                    left = True
                    north = False
                if instructions[r] == "R":
                    right = True
                    north = False
            
            elif south:
                if instructions[r] == "G":
                    start[1] -= 1
                if instructions[r] == "L":
                    right = True
                    south = False
                if instructions[r] == "R":
                    left = True
                    south = False
            elif left:
                if instructions[r] == "G":
                    start[0] -= 1
                if instructions[r] == "L":
                    left = False
                    south = True
                if instructions[r] == "R":
                    north = True
                    left = False
            elif right:
                if instructions[r] == "G":
                    start[0] += 1
                if instructions[r] == "L":
                    right = False
                    north = True
                if instructions[r] == "R":
                    south = True
                    right = False
            r += 1
        if tuple(start) == (0, 0):
            return True
        
        return False



                   
            

