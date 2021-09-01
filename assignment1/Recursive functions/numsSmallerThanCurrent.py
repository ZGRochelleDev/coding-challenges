#Leetcode problem 1365
#How Many Numbers Are Smaller Than the Current Number
#Example of using a frequency array

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sorting
        # nums = [8,1,2,2,3]
        # index: [0,1,2,3,4]
        # nums:  [1,2,2,3,8]
        # output [0,1,1,3,4]
        #dict = {}
        #1: 0
        #2: 1
        #3: 3
        #8: 4
        # final: [4,0,1,1,3]

        """
            -- Brute force solution
            Time complexity: O(n^2) -- number of instructions
            Memory complexity: O(1) -- how much memory you're creating
        
            O(constant) = O(1) = O(1019234) = O(12)
            
            sorting -> n*log(n)

            -- Sort/Map solution
            Time complexity: n*log(n)
            Memory complexity: O(n)
            
            -- Counted Sort
            Time complexity: O(n+k) + n*log(n)
            Memory complexity: O(n) + O(k) = (n+k)
        """

        # the last area of optimization is with our Sort function. Using Counted Sort, we can reduce our time complexity to O(n+k)
        # Because the max val is 100, we know that our frequency array will have a max size of 101.frequency arrays contain unique values.
        # create an array with size equal to the max potential number of i, '100'.
        # iterate through nums, add 1 to freqArr per each occurance of nums[i]
        # generate the desired sorted list based on the values within freqArr
        #[8,1,2,2,3]
        #[0,1,2,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,...,0]
        #[1,2,2,3,8]
        
        # Counted Sort
        sortedNums = []
        freqArr = [0]*101
        for i in range(len(nums)):
            freqArr[nums[i]] = freqArr[nums[i]] + 1
        for i in range(len(freqArr)):
            if freqArr[i] == 0:
                continue
            for each in range(freqArr[i]):
                sortedNums.append(i)

        returnArr = []
        d = {} # dict()
        for x in range(len(sortedNums)):
            if sortedNums[x] in d:
                continue
            d[sortedNums[x]] = x # d.append()
        for each in nums:
            returnArr.append(d[each])
        return returnArr
