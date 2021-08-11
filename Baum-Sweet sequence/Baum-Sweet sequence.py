def baum_sweet(z):
    num_of_zeros = []
    count_of_zeros = []
    if z == "0":
        n = 1
    else:
        for i in z:
            if i == "0":
                num_of_zeros.append(i)
            else:
                count_of_zeros.append(num_of_zeros.count("0"))
                num_of_zeros = []
        count_of_zeros.append(num_of_zeros.count("0"))

        n = 1
        for i in count_of_zeros:
            if i % 2 == 1:
                n = 0
    return n


num = int(input("type a number: "))
baum_sweet_sequence = []
for i in range(num+1):
    x = bin(i)
    z = x[2:]
    baum_sweet_sequence.append(baum_sweet(z))

print(baum_sweet_sequence)
