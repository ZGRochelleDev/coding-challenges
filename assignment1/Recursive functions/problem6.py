# Problem 6
# Write a recursive function that prints all the subsequences of a string
# of length at most 10.
# Example: INPUT: “abc” OUTPUT: “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”

#time complexity:
	# Recursive: O(n^2) - recursive function is called each time we increment x (so, n times);
	# the while loop runs for each increment of y (so, n times). So, O(n^2).
#space complexity:
	# 2 variables (x and y) are placed on the stack for ea. recursive call.
	# we recurse each time we increment x (n times)
	# so I think the Space Com is O(n)
 
#iterative
class Solution:
	def subseqStr(self, s):
		size = len(s)
		print("")
		for x in range(size):
			for y in range(size-x):
				print(s[x:y+1+x])
s = Solution()
test_string = "abc"
s.subseqStr(test_string)

# recursive
# isn't printing out every substring; eg  "ac"
# cant figure out how to do it without a while-loop
class Solution:
	def subseqStr(self, s):
		size = len(s)
		print(" ")
		def recurse(x,y):
			if x > size:
				return 0
			y = x + 1
			while y <= size:
				print(s[x:y])
				y+=1
			recurse(x+1,y)
		recurse(0,0)
			

s = Solution()
test_string = "abc"
s.subseqStr(test_string)
