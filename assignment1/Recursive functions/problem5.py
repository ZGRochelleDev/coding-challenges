#Problem 5 - had to look this one up
#Write a recursive function that takes a variable n and
#returns the number of paths in a grid of size n*n
#starting from (0,0) to (n-1,n-1). (n doesn’t bypass 8)

#question: can we move diagonally, or only sideways?

#time complexity:
# each recursive call traverses a single cell in the grid
# the grid is n length and n height
# Since each cell needs to be traversed in a 2D array, Time Complexity is O(n^2)



#Space Complexity
	# For each recursive call, 2 variables are placed onto the stack
	# the number of times this happens is n times
	# O(2n) or O(n)

class Solution:
	def numberOfPaths(self, m, n):
		print("pass")
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
class Solution2:
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

s2 = Solution2()
#print(s2.traverseGrid(3))