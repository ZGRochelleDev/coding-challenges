# Problem 8
# Write a recursive function that prints out the longest palindromic substring.

#time complexity:
#space complexity:

#iterative approach
class Solution1:
    def __init__(self):
        self.largest = ""
    def check(self,p,q,m):
        s = ""
        for each in range(p,q+1):
            s = s + m[each]
        if s == s[::-1]:
            if len(s) >= len(self.largest):
                self.largest = s
    def isPalindrome(self, s):
        new_str = s.replace(' ', '')
        size = len(new_str)
        for i in range(size):
            for j in range(size-1,0+i,-1):
                if new_str[i] == new_str[j]:
                    self.check(i,j,new_str)
        return self.largest
s = Solution1()

test_string = "ytuxiiqaaqiixytu"
print(s.isPalindrome(test_string))

#recursive approach