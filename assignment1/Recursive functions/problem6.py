# Problem 6
# Write a recursive function that prints all the subsequences of a string
# of length at most 10.
# Example: INPUT: “abc” OUTPUT: “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”

#time complexity:
	# Iterative: O(n^2)
	# Recursive: O(n^2) - recursive function is called x times; while loop runs y times

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

#recursive
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
