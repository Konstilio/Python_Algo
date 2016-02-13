class Solution(object):
    def removeDuplicates(self, nums):
        l = len(nums)
        if l <  2:
            return l
        
        goodIndex = 0
        dupNum = 1
        for k in range(1, l):
            curr = nums[k]
            good = nums[goodIndex]
            
            if curr > good:
                nums[k], nums[goodIndex + 1] = nums[goodIndex + 1], nums[k]
                goodIndex += 1
                dupNum = 1
                continue
            
            elif curr == good and dupNum == 1:
                nums[k], nums[goodIndex + 1] = nums[goodIndex + 1], nums[k]
                goodIndex += 1
                dupNum = 2
                continue

  
        return goodIndex + 1
