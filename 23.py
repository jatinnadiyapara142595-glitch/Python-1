# 3. Function to Calculate Factorial (Using Recursion)
#  Implement factorial using:
# o Normal function
# o Recursive function

def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
