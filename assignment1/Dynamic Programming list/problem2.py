# Problem 2
# Add memoization to the fibonacci function
#time complexity:
    #initial assumption = O(n)
import time
memo = {}
def fibonacciMemo(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        if number - 2 in memo:
            x = memo[number - 2]
        else:
            x = fibonacciMemo(number - 2)
        if number - 1 in memo:
            y = memo[number - 1]
        else:
            y = fibonacciMemo(number - 1)
        memo[number - 2] = x
        memo[number - 1] = y
        return x + y

start = time.time()
print("fibonacciMemo",fibonacciMemo(30))
end = time.time()
print("time:",end - start)