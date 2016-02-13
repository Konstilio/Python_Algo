class Solution(object):
    def bsearch(self, nums, target, l, r):
        
        while l < r:
            mid = (r - l) / 2 + l
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] == target:
            return l
        return -1

def search(self, nums, target):
    size = len(nums)
        
        ##find min
        l = 0
        r = size - 1
        while (l < r):
            mid = (r - l) / 2 + l
            
            if (nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid
    
        #l is min index
        l1 = 0
        r1 = l - 1
        index = self.bsearch(nums, target, l1, r1)
        
        if index == -1:
            l1 = l
            r1 = size - 1
            index = self.bsearch(nums, target, l1, r1)

    return index