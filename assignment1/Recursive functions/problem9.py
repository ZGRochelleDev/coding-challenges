# Problem 9 - not able to implement
# Write a recursive function that finds if a string has a
# palindrome subsequence of length > 1 and returns true if that's the case

#mirror
# if False, keep going

# a 		False
# aa 		True
# axxxa 	continue
# ab 		False
# axxxb		discard and cont

class Solution:
	def isPalindrome(self, n):
		def recurse(s):
			if len(s) <= 1:
				return False
			elif s == s[::-1]:
				return True
			elif s[0] == s[len(s)-1]:
		 		return self.isPalindrome(s[1:len(s)-1])
			else:
				self.isPalindrome(s[1:len(s)-1])
			return False

		return recurse(n.replace(' ', ''))

s = Solution()
test_string = "abba"
# expected largest subString = abba
print(s.isPalindrome(test_string))