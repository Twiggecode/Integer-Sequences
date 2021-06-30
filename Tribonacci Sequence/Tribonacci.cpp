#include <iostream>

int main() {
    //Initialize first three Tribonacci sequence numbers
    int a = 0, b = 0, c = 1;
    
    //User input
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
 
    //value for input 0 (first term) or input 1 (second term)
    if (n == 0 || n == 1) {
        std::cout << "The Nth term in the sequence is 0" << std::endl;
    }

    //value for input 2 (third term)
    else if (n == 2) {
        std::cout << "The Nth term in the sequence is 1" << std::endl;
    }

    //Use equation Tn = Tn-1 + Tn-2 + Tn-3
    else {
        int d;
        for (int i = 0; i < n - 2; i++) {
            d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        std::cout << "The Nth term in the sequence is " << d << std::endl;
    }

    return 0;

}