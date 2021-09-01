#Problem 4 - 4got to do this 1
#Find the max sum of nodes in a path from root to leaf in a BT
'''
   INPUT:
           5 (17)            depth: 0
         /    \
        4 (11)    1(12)        depth: 1
      /  \      / \
     7    2   11   5     depth: 2
    N N  N N  N N  N N 
    
    None
    
    OUTPUT: 17 (5 -> 1 -> 11) 
'''
#recursive
class Solution:
	def maxSum(self, root):
        # returns the maximum sum from root to leaf of node
        def maxSum(node):
            #base case: return when leaf
            if root is None:
                return 0
            # left = maxSum(node.left)
            # right = maxSum(node.right)
            return node.val + max(maxSum(node.left), maxSum(node.right))
        return maxSum(root)