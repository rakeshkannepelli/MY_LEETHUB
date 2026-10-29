class Solution:
    def firstUniqChar(self, s: str) -> int:
        previous ={}
        
        for i in range(len(s)):
            letter = s[i]
            if letter not in previous:
                previous[letter] = 1
            else:
                previous[letter] += 1
        for j in range(len(s)):
            if previous[s[j]] == 1:
                return j
        return -1