def kolakoski(n):
    """
    this implementation uses a space complexity of O(n) and has a
    time complexity of O(n) as given on wikipedia.
    It is also 1-indexed that is, the first element in the sequence has
    an index of 1

    """
    # initial beginning sequence
    kolakoski_sequence = [1, 2, 2]

    def generate_additional_sequence():
        is_even = lambda x: x % 2 == 0
        for i in range(3, n):
            if is_even(i):
                kolakoski_sequence.extend([2] * kolakoski_sequence[i - 1])
            else:
                kolakoski_sequence.extend([1] * kolakoski_sequence[i - 1])

    if n < 1:
        raise IndexError("the sequence is 1-indexed")

    if n in range(1, 4):
        return kolakoski_sequence[n - 1]

    generate_additional_sequence()
    return kolakoski_sequence[n - 1]
