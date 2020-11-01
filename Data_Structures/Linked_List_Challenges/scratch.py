import time
def factorial(n):
    # Base case: 
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_bu(n):
    if n <= 1:
        return 1
    bb = []
    bb.append(1)
    for i in range(1,n+1):
        prod = bb[i-1] * i
        bb.append(prod)
    return bb[n]





if __name__ == "__main__":
    print(factorial(10))
    result = factorial_bu(10)