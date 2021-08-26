# Problem 8
# Write a function that prints out the longest palindromic substring.

#iterate through string, 2 pointer

#time complexity:
	# Initial assumption = O(n^2)
	# Check func is O(n)
	# and it's called O(n) times from within isPalindrome func based on the size of the string

class Solution:
	def __init__(self):
		self.largest = ""
	def check(self,p,q,m):
		st = ""
		while p <= q:
			if (m[p] != m[q]):
				return False
			elif p == q:
				st = st + m[p] + st[::-1]
			else:
				st = st + m[q]
			p+=1
			q-=1
		if len(st) >= len(self.largest):
			self.largest = st
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		size = len(new_str)
		for i in range(size):
			for j in range(size-1,0+i,-1):
				if new_str[i] == new_str[j]:
					self.check(i,j,new_str)
		return self.largest

s = Solution()
test_string = " a b  a x yy  g yzzy g x g yzy g "
# expected largest subString = zygxgyz
print(s.isPalindrome(test_string))