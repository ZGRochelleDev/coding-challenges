# def getCombinations(n):
#     def gen(depth, buffer):
#         if depth == n:
#             print(buffer)
#             return
#         gen(depth+1,buffer+"0")
#         gen(depth+1,buffer+"1")
#     gen(0, "")

# n = 3
# getCombinations(n)

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

# # testSet = [5,8,11]
# # [0:1] = 5
# # [1:2] = 8
# # [2:3] = 11

# INPUT: [1,2,3]
# OUTPUT: [] [1] [2] [3] [1,2] [1,3] [2,3] [1,2,3]

# INPUT: [1,2]
# OUTPUT: [] [1] [2] [1,2]

# INPUT: [1]
# OUTPUT: [] [1]
# Generate all the possible combinations of binary digits of length n
# INPUT: 3
# OUTPUT: 000 001 010 011 100 101 110 111

# INPUT: 2
# OUTPUT: 00 01 10 11

# INTPUT: 1
# OUTPUT: 0 1

# base case: return 1
# if ones digit = 1 then set 10s place = 1 and 1's = 0
# return if all == 1
'''


Time: O(2^n) | number of times the recursive function is called * complexity of the recursive function 

Memory: O(n) | we have a tree with a known depth, the stack will have at most depth stacked recursive functions at the same time which is n cuz each recursive call is appending a character
    n = 2
           .            depth: 0
         /0   \1
        0 #1      1 #2       depth: 1
      /0  \1   /0 \1
      00  01   10   11  depth: 2
      #3  #4   #5    #6
      
      stack: []
           []            depth: 0
         /.   \1
        []      [1]       depth: 1
      /.  \2   /. \2
      []  [2] [1]  [1,2]  depth: 2   
   depth:    | 
    arr = [1,2] 
     
'''
# return recurse(val) + recurse(val)

# def getCombinations(n):
#     def gen(depth, buffer):
#         if depth == n:
#             print(buffer)
#             return
#         gen(depth+1,buffer+"0")
#         gen(depth+1,buffer+"1")
#     gen(0, "")

# n = 3
# getCombinations(n)

   