class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # Sort the array to use the two-pointer technique
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Optimization: if the current number is positive, no sum can be zero with remaining positive numbers
            if nums[i] > 0:
                break
                
            j = i + 1
            k = n - 1
            
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                
                if total_sum < 0:
                    j += 1 # Sum is too small, increment left pointer
                elif total_sum > 0:
                    k -= 1 # Sum is too large, decrement right pointer
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicate values for j and k pointers
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                        
                    # Move both pointers inward to find new unique triplets
                    j += 1
                    k -= 1
                    
        return result
