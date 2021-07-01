def main():
    """
    print the nth prime number, where n is a non-negative integer
    indexing starts at zero, so if n == 0 print the first prime number
    """

    # take user input
    error_message = "Invalid input, please enter a non-negative integer"

    try:
        n = int(input("Please enter a non-negative integer: "))
    except: # n must be an integer
        print(error_message)
        return

    if n < 0: # n cannot be less than zero
        print(error_message)
        return

    # if n == 0 print the first prime number
    # n == 1 print the second prime number and so on...
    count = 0 # number of prime numbers seen so far
    number = 2 # prime numbers start from 2

    while True:
        if is_prime(number): # found a prime number
            count += 1
            if count == n + 1: # found the prime number the user asked for 
                print(number)
                return
        
        number += 1



def is_prime(n):
    """returns True if n is prime, False otherwise"""
    
    for i in range(2, n):
        if n % i == 0: # not a prime number
            return False
    
    # if we reached so far, the number should be a prime number
    return True


if __name__ == "__main__":
    main()
