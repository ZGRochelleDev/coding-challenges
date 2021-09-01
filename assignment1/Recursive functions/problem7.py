# Problem 7
# Write a function that determines if a String is a palindrome
# INPUT: “ASISA” OUTPUT: True , INPUT: “SSA” OUTPUT: False. 
# Write an iterative and a recursive function that returns bool.

#time complexity:
	# Recursive: O(n) - the recusive function is called for half the length of the string.
#space complexity:

#recursive
class Solution:
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		size = len(new_str)-1
		def compareLetters(i,j):
			if i < j:
				if new_str[i] != new_str[j]:
					return False
			else:
				return True
			return compareLetters(i+1,j-1)
		return compareLetters(0,size)

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
