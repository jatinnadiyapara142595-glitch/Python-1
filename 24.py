# 4. Function with Default Arguments
#  Write a function to calculate simple interest.
#  Keep rate default as 5%.

def simple_interest(p, t, r=5):
    return (p * t * r) / 100

# Example
principal = float(input("Enter Principal: "))
time = float(input("Enter Time: "))

print("Simple Interest:", simple_interest(principal, time))
