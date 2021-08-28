#Problem 1
#Write a recursive function that returns the frequency of a key given as input in a BST

# Time Complexity: O(n)
# Regardless of what happens the entire tree must be traversed,
# since we are counting the occurrence, not simply searching for 1 node.

# Space Complexity: O(h)
# The function makes 1 recursive call per each node.
# Each recursive call is placed onto the stack.
# Then removed after each subtree has finished recursing (left then right).
# Therefore, the memory is proportionate to the height of the tree O(h).

# recurse return the result without the global variable
class Solution:
	def countKeyInBST(self,key,root):
		def countFreq(node):
			if node is None:
				return []
			elif node.val == key:
				self.count += 1
			return [node.val] + countFreq(node.left) + countFreq(node.right)
		return countFreq(root)

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

