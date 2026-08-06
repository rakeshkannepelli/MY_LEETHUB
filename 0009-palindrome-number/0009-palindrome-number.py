class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        rev=num[::-1]
        return True if num==rev else False