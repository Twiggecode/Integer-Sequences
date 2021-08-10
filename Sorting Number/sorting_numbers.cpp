#include <iostream>
#include <cmath>

//Function to find Sn
int sn(int n)
{
    return std::floor(1 + std::log2(n));
}

//Implementing the formula of a sorting number
int sorting_number(int n)
{
    return n * sn(n) - int (std::pow(2, sn(n))) + 1;
}

void print_sequence_sorting_numbers(int n)
{
    for (int i = 1; i <= n+1; i++)
    {
        std::cout << sorting_number(i) << std::endl;
    }
}

int main() {
    int n;
    std::cout << "Enter the number of elements of sorting numbers you want: ";
    std::cin >> n;
    if (std::cin.fail()) {
        std::cout << "Please enter a valid number. " << std::endl;
    }

    print_sequence_sorting_numbers(n);
}
