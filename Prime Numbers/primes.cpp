#include <limits> // Required for ignoreLine function
#include <iostream>
/*
 * A program that prompts the user for a number and checks the number
 * for primality. Returns true if the number is prime, returns false
 * if the number is not prime.
 *
 * 2147483647 is the highest 32 bit signed integer that is prime.
 * This code takes 2.4 - 2.5 secs to return true (prime) on my computer.
 */

// Function declarations
int getUsersNumber();
void ignoreLine();
bool checkIfPrime(int isItPrime);
void printResult(int number, bool result);

int main()
{
    int usersNumber{getUsersNumber()}; // Get users number to check
    bool isPrime{checkIfPrime(usersNumber)}; // Check useres Number
    printResult(usersNumber, isPrime);

    return 0;
}

/**
 * Prompts the user to enter a positive number greater than 1
 * If a non number or integer less than 2 is entered the input
 * fails. This failure is cleared and reset to normal non-fail
 * mode and the input / any remaining inputs are cleared. The user
 * is then asked again to enter an integer
 */
int getUsersNumber()
{
    while (true)
    {
        std::cout << "Enter a positive integer greater than 1: ";
        int number{};
        std::cin >> number;

        // Checks if user inputted an incorrect char, if not
        // returns the users inputed integer
        if (std::cin.fail())
        {
            std::cin.clear(); // since we failed, this puts us back to normal
            ignoreLine(); // clears the bad input and any remaining chars
        }
        else
        {
            ignoreLine(); // clears any remaining chars
            return number;
        }
    }
}

/**
 * function to clear any reamining chars in input
 * requires #include <limits>
 */
void ignoreLine()
{
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

/**
 * Checks if isItPrime is 2 and returns true if it is 2.
 * Checks if isItPrime is even and returns false if it's even.
 * Checks if isItPrime is evenly divisable by a number less than
 * half isItPrime (isItPrime / 2), if this is true the number is not prime
 * and the function returns false. A numerator (isItPrime) will not be evenly
 * divisable by a denominator (i) whose value is greater than or equal to the
 * numerator, in this case the numerator is a prime number and the function
 * returns true.
 *
 * n / i : n is prime if i >= (n / 2) and (n / i) != 0 for 3 <= i < (n / 2)
 *
 * 2147483647 highest 32 bit signed prime integer
 */
bool checkIfPrime(int isItPrime)
{
    if (isItPrime == 2)
        return true;
    else if (isItPrime < 2 || isItPrime % 2 == 0)
        return false;

    // We start at 3 as we've already checked if the number is 2,
    // less than 2 or even. We iterate by two checking with only
    // odd numbers. This saves time, if only for large values.
    for (int i{3}; i < (isItPrime >> 1); i += 2)
        if (isItPrime % i == 0)
            return false;

    return true;
}

/**
 * Prints the the users number  and whether it is a prime or non-
 * prime number.
 */
void printResult(int number, bool result)
{
    std::cout << number << " is";

    if (result)
        std::cout << " prime.\n";
    else if (!result)
        std::cout << " not prime.\n";
}
