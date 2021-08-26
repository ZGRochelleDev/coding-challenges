# Problem 10 - not able to implement
# Write a recursive function that prints all the palindrome
# subsequences of a string that is of length at most 8 without
# duplicates and ordered by the length of the subsequence.
# Example: INPUT: “aaba”. OUTPUT: ‘a’, ‘b’, ‘aa’, ‘aba’

#mirror
class Solution:
	def __init__(self):
		self.largest = ""
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		if new_str == new_str[::-1]:
			return new_str
		else:
			size = len(new_str)
			for i in range(size):
				for j in range(size-1,0+i,-1):
					if new_str[i] != new_str[j]:
						continue
					elif new_str[i] == new_str[j]:
						self.isPalindrome(new_str[i:j+1])
						#self.check(new_str[i:j+1])
		return self.largest

s = Solution()
test_string = " a b  a x yy  g yzzy g x g yzy g "
# expected largest subString = zygxgyz
print(s.isPalindrome(test_string))