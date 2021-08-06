import itertools

sequence_array = []


def recaman(a: int):

    if a == 0:
        sequence_array.append(a)
    elif (
        a > 0
        and sequence_array[a - 1] - a > 0
        and sequence_array[a - 1] - a not in sequence_array
    ):
        sequence_array.append(sequence_array[a - 1] - a)
    else:
        sequence_array.append(sequence_array[a - 1] + a)
    return sequence_array


if __name__ == "__main__":
    n = int(input("Enter integer value: "))
    if n < 0:
        exit("Error input. Please enter a non-negative integer value!")
    gen = (recaman(x) for x in range(n + 1))
    index = n
    res_arr = next(itertools.islice(gen, index, None))
    res = res_arr[index]
    print(res)

    # print(next(gen))
