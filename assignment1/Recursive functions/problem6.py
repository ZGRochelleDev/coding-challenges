# Problem 6
# Write a recursive function that prints all the subsequences of a string
# of length at most 10.
# Example: INPUT: “abc” OUTPUT: “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”

# Time complexity:
# Time Complexity: O(n^2)
# Explanation: This represents the "number of times the recursive function is called" * "th complexity of the recursive function"

# Space complexity: O(n)
# We know the depth of the tree, the stack will have at most depth stacked
# recursive functions at the same time which is 'n',
# since each recursive call is appending a new character.

# Recursive approach
class Solution:
	def subseqStr(self, s):
		size = len(s)
		print(" ")
		def gen(idx, buffer):
			if idx == len(s):
				print(buffer)
				return
			gen(idx+1,buffer) # increment idx, append to buffer
			gen(idx+1,buffer + [s[idx]])
		gen(0, [])

test_string = "abc"
s = Solution()
s.subseqStr(test_string)


#This is the same solution as what we worked on together below on - 8/28
class Solution:
    def subsetOfArray(self,arr):
        
        self.count = 0
        def gen(idx, buffer):
            #global count
            self.count += 1
            if idx == len(arr):
                print(buffer)
                return
            # increment idx, append to buffer
            gen(idx+1,buffer)
            gen(idx+1,buffer + [arr[idx]])
 
        gen(0, [])
        print(self.count)

testSet = [1, 2, 3]
s = Solution()
s.subsetOfArray(testSet)