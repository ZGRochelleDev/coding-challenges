# Problem 8
# Write a recursive function that prints out the longest palindromic substring.

#time complexity:
#space complexity:

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
		
		# i = 0
		# j = len(new_str)-1
		# while i <= j:
		# 	if new_str[i] == new_str[j]:
		# 		self.check(i,j,new_str)
		# 		print(new_str[i],i,"-",new_str[j],j)
		# 	i+=1
		# 	j-=1

		size = len(new_str)
		for i in range(size):
			for j in range(size-1,0+i,-1):
				if new_str[i] == new_str[j]:
					print(new_str[i],i,"-",new_str[j],j)

					self.check(i,j,new_str)
		return self.largest

s = Solution()

test_string = "ytuxiiqaaqiixytu"
print(s.isPalindrome(test_string))

# test_string = "ytuxiiqaaqiixytu"
# expected "xiiqaaqiix"
# produces "xiiqa"

# test_string = "abaxyygyzzygxgyzyg "
# expected "zygxgyz"
# produces "zygxgyz"