#Problem 5 - had to look this one up
#Write a recursive function that takes a variable n and
#returns the number of paths in a grid of size n*n
#starting from (0,0) to (n-1,n-1). (n doesn’t bypass 8)

#question: can we move diagonally, or only sideways?

#time complexity:
	# each recursive call iterates through a path of size n
	# they are then added at the end n + n = 2n
	# Initial assumption = O(n)

class Solution:
	def numberOfPaths(self, m, n):
		if(m == 1 or n == 1):
			return 1
		return self.numberOfPaths(n-1, m) + self.numberOfPaths(m, n-1)
		#+ self.numberOfPaths(m-1, n-1)

s = Solution()
n = 3
print(s.numberOfPaths(n, n))



#***Attempt 1***
#create an array to store previously visited cells
#start at position 00
#check neighbor 1
#if neghbor 1 is target, return previously visited array
#else if neighbor 1 is in prev visited, then check other neighbor
#else if neighbor 1 not in previously visited
#add it to previously visited then
#move to that position


#iterative approach
class Solution:

	def createGrid(self,size):
		dictGrid = {}
		for x in range(size):
			for y in range(size):
				dictGrid[x,y]=str(x)+str(y)
		return dictGrid
	
	def traverseGrid(self,n):
		grid = self.createGrid(n)
		prevVisited = []
		x = 0
		y = 0
		end = str(n-1)+str(n-1)
		prevVisited.append(grid[x,y])
		while True:
			#if right within bounds check right
			if y < n-1 and grid[x,y+1]:
				prevVisited.append(grid[x,y+1])
				if grid[x,y+1] == end:
					return prevVisited
				print("current pos =",grid[x,y+1])
				y = y + 1
			#otherwise
			#if left within bounds check left
			elif x < n-1 and grid[x+1,y]:
				prevVisited.append(grid[x+1,y])
				if grid[x+1,y] == end:
					return prevVisited
				print("current pos =",grid[x+1,y])
				x = x + 1
			else:
				return "Fail"


s = Solution()
print(s.traverseGrid(3))
