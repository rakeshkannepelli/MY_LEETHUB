class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x , y = 0 , 0
        for move in moves:
            if move == 'U':
                y = y + 1
            if move == 'D':
                y = y - 1
            if move == 'L':
                x = x - 1
            if move == 'R':
                x = x + 1
        if x == 0 and y == 0:
            return True 
        else:
            return False