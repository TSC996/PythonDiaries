# Fibonaaci Numbers, where the a number is the sum of two preceding numbers
# This program finds the nth Fibonacci Number
# I have Considered '0' as the First Fibonacci Number
def Fibonacci(n):
    if n < 0:
        print("Incorrect Input")
    # Taking 0 as the first Fibonacci Number
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


a = int(input("Enter a positive integer: "))
print(Fibonacci(a))
