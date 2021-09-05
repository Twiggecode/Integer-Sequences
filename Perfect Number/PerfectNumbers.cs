using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntegerSequencesOpenSourceContributing
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true) // repeating until user input is letter "q"
            {
                Console.WriteLine("Enter the value of n.\nTo quit type 'q'.");
                string input = Console.ReadLine(); // Reading input value
                if (input == "q") // if input is letter "q" canceling the program
                    break;
                if (!Int32.TryParse(input, out int n)) // start new loop, if user input can't be parsed to int
                {
                    Console.WriteLine("Invalid input: Please enter an integer input.");
                    continue;
                }
                bool res;
                try
                {
                    res = IsPerfectNumber(n); // compute result
                    Console.WriteLine("Result = " + res);
                }
                catch(ArgumentOutOfRangeException ex) //start new step of loop, if input value isn't a positive number
                {
                    Console.WriteLine($"Invalid input, please enter a positive number. Your input is {ex.ActualValue}");
                    continue;
                }
                Console.WriteLine("\nPress any key to continue.");
                Console.ReadKey();
                Console.WriteLine();
            }
        }

        // perfect number computing function
        static bool IsPerfectNumber(int n)
        {
            if (n <= 0)
            {
                throw new ArgumentOutOfRangeException("n", n, "");
            }
            int sum = 0;
            for (int i = n - 1; i > 0; i--)
            {
                if (n % i == 0)
                {
                    sum += i;
                }
            }
            return sum == n;
        }
    }
}
