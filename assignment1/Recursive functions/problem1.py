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
	# Upon research = O(n)
		# h is height
#memory complexity:
class Solution:
	def countKeyInBST(self,key,root):
		#self.count = 0
		# return True if key is in BST otherwise False
		def contains(node, key):
			# check for none
			# if node == key return
			if node is None:
				return False
			if node.val == key:
				return True

			if key < node.val:
				 return contains(node.left, key)
			elif key > node.val:
				 return contains(node.right, key)

		# a BST is balanced if the difference between the depth of its right subtree
		# and its left subtree is no more than 1 for every node

		# return the frequency of key in BST
		def countFreq(node, key):
			# base case done
			if node is None:
				return 0	
			# recursive case
			left = countFreq(node.left, key)
			right = countFreq(node.right, key)
			# node.val == key ? 1 : 0
			return left + right + 1 if node.val == key else 0

			# if node is None:
			# 	return []
			# #elif node.val == key:
			# 	#self.count += 1
			# return [node.val] + countFreq(node.left) + countFreq(node.right)
		return countFreq(root, key)
		#return self.count

''' BT -> consider this a Binary Tree

		   5			level 0: 1
		 /  \
		3     7			level 1: 2
	  /  \   / \
 	 2   3  6   3		level 2: 4

 	 level h: 2^h nodes if we assume that the BST is perfect
 	 n = 2^h -> h = log2(n)
 	 if our BST is balanced (perfect BST is balanced ofc) then it's height is log(n)

'''

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

