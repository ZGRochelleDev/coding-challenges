#Problem 3
#Find the subsets of an array of integers using recursion

#time complexity:
	# iterative: we we only have to iterate through the array once = O(n)
	# recursion: the number of times the function is called
	# is based on the size of the array, this is linear, Initial assumption = O(n)

#iterative solution 1st
#move the subarray along the main array comparing the 1st element to each other
#if match then check the next one, and so on...

#recursive method 2nd
#slide a window along mainArr, width = length of subArr
#compare the 2 sections, increment by 1 until a match is found

#iterative
'''
class Solution:
	def subsetOfArray(self,mainArr,subArr):
		p1 = 0
		p2 = 0
		while p1 < len(mainArr):
			if mainArr[p1] == subArr[p2]:
				if p2 == len(subArr)-1:
					return mainArr[p1-p2:p1+1]
				p1+=1
				p2+=1
			else:
				p2 = 0
				p1+=1
		return "no match"

mainArr = [5,8,7,6,10,11]
subArr = [7,6,10]

s = Solution()
print(s.subsetOfArray(mainArr,subArr))

#recursive
class Solution:
	def subsetOfArray(self,mainArr,subArr):
		def countSubsets(m,x,y):
			if y > len(mainArr): #check if out of bounds
				return "no match"
			elif m[x:y] == subArr: #check if match
				return "True at mainArr pos", x
			else: #recurse
				return countSubsets(m,x+1,y+1)
		return countSubsets(mainArr,0,len(subArr))

mainArr = [5,8,11,7,6,10]
subArr = [7,6,10]

s = Solution()
print(s.subsetOfArray(mainArr,subArr))

'''
#recursive2

class Solution:
	def subsetOfArray(self,tSet):
		def countSubsets(x,y):
			if x > len(tSet)-1: #if end of x
				return [ ]
			elif y > len(tSet)-1: #if end of y
				print(tSet[x:y])
				x = x+1
				return countSubsets(x,1+x)
			else:
				print(tSet[x:y])
				return countSubsets(x,y+1+x)
		return countSubsets(0,1)

# testSet = [5,8,11]
# [0:1] = 5
# [1:2] = 8
# [2:3] = 11

testSet = [5,8,11]
s = Solution()
print(s.subsetOfArray(testSet))

#expeted:

#[ ]
#[5,8,11]
#5,8
#5,11
#8,11
#5
#8
#11