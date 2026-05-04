# problem 9 
# recursive fibonacci with memoization 

def fibo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

print(fibo(10))

# memoization saves previous results so its faster 
# without it recursion is very slow