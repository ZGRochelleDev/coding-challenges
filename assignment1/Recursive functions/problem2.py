#Problem 2
#Find the number of unique paths from a the root til the end of the BST

#Counting the leafs will give us the same number?

#1 Recurse through the tree checking each node to see if it has children.
#2 Keeping track of the occurances using a variable.
#3 Return the variable

#time complexity:
	# BST Searching = O(logn)
	# number of nodes = n
	# we have to traverse the entire tree
	# Initial assumption = O(n)

class Solution:
	def countPaths(self,node):
		if node is None:
			return 0
		if node.left is None and node.right is None:
			return 1
		return self.countPaths(node.left) + self.countPaths(node.right)

		#    5			level 0: 1
		#  /  \
		# 3     7			level 1: 2
	 #  /  \   / \
 	#  2   4  6   3		level 2: 4
    # /
   #  1

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
root.left.left.left = Node(1)

s = Solution()
print(s.countPaths(root))