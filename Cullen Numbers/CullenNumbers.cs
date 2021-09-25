using System;

namespace IntegerSequences.CullenNumbers
{
    class CullenNumbers
    {
        // The first few Cullen numbers are: 1, 3, 9, 25, 65, 161, 385, 897, 2049, 4609, 10241, 22529, 49153, 106497
        private static double Cullen(int n)
        {
            return n * Math.Pow(2, n) + 1;
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

            String s = String.Format("The {0}th element from Cullen numbers is {1}", nTH + 1, Cullen(nTH));
            Console.WriteLine(s);
        }
    }
}
