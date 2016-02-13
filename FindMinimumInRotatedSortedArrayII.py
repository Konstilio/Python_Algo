class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (r - l) / 2 + l
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                if nums[r-1] > nums[r]:
                    return nums[r]
                else:
                    r -= 1
        
        return nums[l]

