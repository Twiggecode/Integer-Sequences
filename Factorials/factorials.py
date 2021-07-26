"""
In python default recursion limit is 1000. 
Naive recursive implementation will raise RecursionError for numbers >= 1000.
By using memoization we can calculate factorials of those numbers 
step by step as shown in the main block.
"""

def factorial(a:int, results={}):
    """
    handle edge case
    a == 0 or 1 or -ve number
    """
    if a in results:
        return results[a]

    if a == 0 or a == 1:
        return 1

    if a<0:
        return "Negative Integer is not allowed"

    # recursive call
    result = a * factorial(a-1)

    # memoize the result
    results[a] = result

    return result


if __name__ == "__main__":
    n = 9
    answer = factorial(n)
    print(f"{n}! = {answer}")

    n = 900
    answer = factorial(n)
    print(f"{n}! = {answer}")

    n = 999
    answer = factorial(n)
    print(f"{n}! = {answer}")
