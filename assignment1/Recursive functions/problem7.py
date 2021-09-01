# Problem 7
# Write a function that determines if a String is a palindrome
# INPUT: “ASISA” OUTPUT: True , INPUT: “SSA” OUTPUT: False. 
# Write an iterative and a recursive function that returns bool.

# time complexity: O(n)
# - the recursive function is called O(n/2), which can be reduced to O(n)

# space complexity: O(n)
# - For each recursive call, 2 variables (i and j) are placed onto the stack.
# - They remain until the string is fully traversed or returns false
# - A 20 char string will produce 10 calls on the stack.

#recursive approach
class Solution:
	def isPalindrome(self, s):
		
		def compareChars(i,j):
			if(i < j):
				if(new_str[i] != new_str[j]):
					return False
				else: #check next pair
					return compareChars(i+1,j-1)
			return True

		new_str = s.replace(' ', '')
		return compareChars(0, len(new_str)-1)

s = Solution()
test_string = " a bc b  a"
print(s.isPalindrome(test_string))


'''
# mirror approach
class Solution:
	def isPalindrome(self, s):
		new_str = s.replace(' ', '')
		return new_str == new_str[::-1]
s = Solution()
test_string = " a b  a"
print(s.isPalindrome(test_string))

# iterative approach
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