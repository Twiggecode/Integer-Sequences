"""
Calculate nth Fibonacci term
"""

class NegativeNumber(Exception):
    pass

def fibonacci_iter(n):
    """ Iterative implementation of Fibonacci """
    a, b = 0, 1

    if n < 0:
        raise NegativeNumber('Fibonacci not defined for negative numbers!')
        
    if n == 0:
        return 0

    for _ in range(1, n):
        a, b = b, a + b 
    
    return b


def fibonacci_naive_recur(n):
    """ Naive recursive computation of Fibonacci.
    Time complexity is O(1.6180 ^ n). It's big! """

    if n < 0:
        raise NegativeNumber('Fibonacci not defined for negative numbers!')

    if n < 2:
        return n

    return fibonacci_naive_recur(n - 1) + fibonacci_naive_recur(n - 2)


def fibonacci(n, cache={}):
    """ Memoized recursive computation of Fibonacci.
    Time complexity is O(n). Better! """
    if n < 0:
        raise NegativeNumber('Fibonacci not defined for negative numbers!')

    if n < 2:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


def tests(fib):
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

if __name__ == '__main__':
    tests(fibonacci_iter)
    tests(fibonacci_naive_recur)
    tests(fibonacci)
    print(fibonacci_iter(10000))
