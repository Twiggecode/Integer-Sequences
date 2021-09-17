using System;

namespace IntegerSequences.FermatNumbers
{
    class FermatNumbers
    {
        // The first few Fermat numbers are: 3, 5, 17, 257, 65537, 4294967297, 18446744073709551617, 340282366920938463463374607431768211457
        private static double Fermat(int n)
        {
            return (Math.Pow(2, Math.Pow(2, n))) + 1;
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("Please enter an integer n where n >= 0");
            bool isValid = false;
            int nTH = 0;
            
            while(!isValid) // Check if user input an integer. If not, tries again until an integer is inputted 
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
            String s = String.Format("The {0}th element from Fermat numbers is {1}", nTH + 1, Fermat(nTH));
            Console.WriteLine(s);
        }
    }
}
