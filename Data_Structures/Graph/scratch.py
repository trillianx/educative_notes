def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_dp(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_dp(n-1, memo) + fib_dp(n-2, memo)
        memo[n] = result
        return result

if __name__ == "__main__":
    import time
    start = time.time()
    print(fib(40))
    end = time.time()
    print(end - start)
    start = time.time()
    print(fib_dp(40))
    end = time.time()
    print(end - start)