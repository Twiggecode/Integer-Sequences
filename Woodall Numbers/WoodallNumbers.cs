using System;

namespace IntegerSequences.WoodallNumbers
{
    class WoodallNumbers
    {
        // The first few Woodall numbers are: 1, 7, 23, 63, 159, 383, 895, 2047, 4607
        private static double Woodall(int n)
        {
            n++; // Woodall formulas works with n >= 1
            return n * Math.Pow(2, n) - 1;
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("Please enter an integer n where n >= 0");
            bool isValid = false;
            int nTH = 0;

            while (!isValid) // Check if user input an integer. If not, tries again until an integer is inputted 
            {
                try
                {
                    string input = Console.ReadLine();
                    nTH = int.Parse(input);
                }
                catch (FormatException)
                {
                    Console.WriteLine("Please enter an intenger n where n >= 0");
                    continue;
                }
                isValid = true;
            }
            String s = String.Format("The {0}th element from Fermat numbers is {1}", nTH + 1, Woodall(nTH));
            Console.WriteLine(s);
        }
    }
}
