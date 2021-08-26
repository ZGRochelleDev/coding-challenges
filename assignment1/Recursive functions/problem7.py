# Problem 7
# Write a function that determines if a String is a palindrome
# INPUT: “ASISA” OUTPUT: True , INPUT: “SSA” OUTPUT: False. 
# Write an iterative and a recursive function that returns bool.

#time complexity:
	# Recursive: O(n) - the recusive function is called O(n/2),
	# which can be reduced to O(n)

#recursive
class Solution:
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		size = len(new_str)-1
		def recurse(i,j):
			if i < j:
				if new_str[i] != new_str[j]:
					return False
			else:
				return True
			return recurse(i+1,j-1)
		return recurse(0,size)

s = Solution()
test_string = " a c b  a"
print(s.isPalindrome(test_string))


#mirror
'''
class Solution:
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		return new_str == new_str[::-1]
s = Solution()
test_string = " a b  a"
print(s.isPalindrome(test_string))
'''

#iterative
'''
class Solution:
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		i = 0
		j = len(new_str)-1
		while i <= j:
			if (new_str[i] != new_str[j]):
				return False
			i+=1
			j-=1
		return True
s = Solution()
test_string = " a bc  a"
print(s.isPalindrome(test_string))
'''
