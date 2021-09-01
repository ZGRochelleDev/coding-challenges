#Problem 4
#Find the max sum of nodes in a path from root to leaf in a BT

#Time: O(n
    # - All nodes need to be traversed to find the max sum
#Space: O(h)
    # - The function recurses once for each node and continues until it reaches the leaf.
    # - The height of the tree from root to leaf determines the max stack size

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
        def calculateMaxSum(node):
            #base case: return when leaf
            if root is None:
                return 0

            left = calculateMaxSum(node.left)
            right = calculateMaxSum(node.right)

            return node.val + max(left, right)

        return calculateMaxSum(root)