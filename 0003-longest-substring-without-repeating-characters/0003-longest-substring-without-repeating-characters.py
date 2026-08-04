class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window pattern
        n=len(s)
        longest=0
        left=0
        set_=set()

        for right in range(n):
            while s[right] in set_:
                set_.remove(s[left])
                left +=1

            w=(right-left)+1
            longest=max(longest,w)
            set_.add(s[right])

        return longest