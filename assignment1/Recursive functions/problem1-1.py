#Problem 1-1
#Write a contains function for a BST

#time complexity:
	# BST Searching = O(logn)
	# number of nodes = n
	# Initial assumption = O(n logn)
	# Upon research = O(n)
		# h is height
	#worst: O(n) - in the event that we had to traverse the entire tree to find the val
	#Best: O(1) - if the val we're looking for is in the Root node
	#Average: O(logn) - assuming the tree is balanced; the number of nodes increases exponentially proportunate to the height, 2^0, 2^1, 2^2 etc

[O(n),O(logn)]
Worst: O(n), in the event that we had to traverse the entire tree to find the val. Average: O(logn), assuming the tree is balanced; the number of nodes increases exponentially proportionate to the height, 2^0, 2^1, 2^2 etc. Best: O(1), if the val we're looking for is in the Root node.

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
		return countFreq(root, key), contains(root, key)
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
print(s.countKeyInBST(4,root))