# Problem 1
# Write the fibonacci recursive function without memoization.
#time complexity:
	#initial assumption = O(n)
	#upon research = O(2^n)

import time
def fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return (fibonacci(number - 2) + fibonacci(number - 1))
start = time.time()
print("fibonacci",fibonacci(30))
end = time.time()
print("time:",end - start)