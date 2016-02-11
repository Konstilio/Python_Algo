class Solution(object):
    def recountMax(self, tempMaxRobPrev, tempMaxNotRobPrev, num):
        return (tempMaxNotRobPrev + num, max(tempMaxNotRobPrev, tempMaxRobPrev))
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        #robbed first
        maxRobPrev = nums[1]
        maxNotRobPrev = nums[0]
        
        for i in range(2, len(nums) - 1):
            (maxRobPrev, maxNotRobPrev) = self.recountMax(maxRobPrev, maxNotRobPrev, nums[i])
            
        FirstMax = max(maxRobPrev, maxNotRobPrev)
        
        #not robbed first
        maxRobPrev = nums[1]
        maxNotRobPrev = 0
        
        for i in range(2, len(nums)):
            (maxRobPrev, maxNotRobPrev) = self.recountMax(maxRobPrev, maxNotRobPrev, nums[i])
            
        SecondMax = max(maxRobPrev, maxNotRobPrev)
        
        return max(FirstMax, SecondMax)
