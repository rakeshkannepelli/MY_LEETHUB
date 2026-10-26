class Solution:
    def calPoints(self, operations: list[str]) -> int:
        final = []
        
        for i in operations:
            if i == "+":
                final.append(final[-1] + final[-2]) 
            elif i == "C":
                final.pop()
            elif i == "D":
                final.append(final[-1] * 2)
            else:
                final.append(int(i))
                
        return sum(final)