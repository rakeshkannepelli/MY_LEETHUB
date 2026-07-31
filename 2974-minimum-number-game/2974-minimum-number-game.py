class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for num in range(0,len(nums)-1,2):
            nums[num] , nums[num + 1] = nums[num + 1 ] , nums[num]
        return nums