using System;

namespace IntegerSequences.CarolNumbers
{
    class carol_number
    {
        // The first few Carol numbers are: −1, 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527 (sequence A093112 in the OEIS).
        private static double Carol(int n)
        {
            n++; // if n == 0 then returns a wrong value
            return (Math.Pow(Math.Pow(2, n) - 1, 2)) - 2;
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
                    Console.WriteLine("Please enter an integer n where n >= 0");
                    continue;
                }
                isValid = true;
            }
            String s = String.Format("The {0}th element from Carol numbers is {1}", nTH + 1, Carol(nTH));
            Console.WriteLine(s);
        }
    }
}
