class Solution(object):
    
    def RecursiveSum(self, node, currSum, TargetSum):
        if node == None:
            return False
        
        currSum += node.val
        if node.left == None and node.right == None:
            return currSum == TargetSum
            
        return (self.RecursiveSum(node.left, currSum, TargetSum) or self.RecursiveSum(node.right, currSum, TargetSum))
            
    
    def hasPathSum(self, root, sum):
        return self.RecursiveSum(root, 0, sum)
