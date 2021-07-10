# Program to find Juggler Sequence in Python
# Juggler Sequence: https://en.wikipedia.org/wiki/Juggler_sequence
# The juggler_sequence function takes in a starting number and prints all juggler
# numbers starting from that number until it reaches 1
 
# Keep in mind that the juggler sequence has been conjectured to reach 1 eventually
# but this fact has not yet been proved

def juggler_sequence(n):
    seq = [n]
    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(int(seq[-1] ** 0.5))
        else:
            seq.append(int(seq[-1] ** 1.5))

    return seq

if __name__ == '__main__':
    x = int(input("Enter a number for Juggler Sequence: "))
    print(juggler_sequence(x))