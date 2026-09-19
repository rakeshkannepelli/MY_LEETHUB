class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        final = 0
        
        for i in range(n):
            ans = start + 2 * i
            nums.append(ans)
            final = ans ^ final

        return final