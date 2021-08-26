#Problem 1
#Write a recursive function that returns the frequency of a key given as input in a BST

#How many times does a number appear in a BST using recursion?
#1 Recurse through the tree checking for the key during each loop.
#2 Keeping track of the occurances using a variable.
#3 Return the variable

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#time complexity:
	# BST Searching = O(logn)
	# number of nodes = n
	# Initial assumption = O(n logn)
	# Upon research = O(h logn)
		# h is height
#memory complexity:

# recurse return the result without the global variable

class Solution:
	def countKeyInBST(self,key,root):
		#self.count = 0
		def recurse(node):
			
			if node is None:
				return []
			elif node.val == key:
				self.count += 1
			return [node.val] + recurse(node.left) + recurse(node.right)
		return recurse(root)
		#return self.count

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)
root.right.left = Node(6)

s = Solution()
print(s.countKeyInBST(10,root))

