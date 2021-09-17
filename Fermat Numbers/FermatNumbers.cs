using System;

namespace IntegerSequences.FermatNumbers
{
    class FermatNumbers
    {
        private static double Fermat(int n)
        {
            return (Math.Pow(2, Math.Pow(2, n))) + 1;
        }

        public static void Main(string[] args)
        {
            // This method returns the nth element of the Fermat numbers where n is a positive integer (or zero) input by the user
            Console.WriteLine("Please enter an intenger n where n >= 0");
            bool isValid = false;
            int nTH = 0;
            
            while(!isValid)
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
            String s = String.Format("The {0}th element from Fermat numbers is {1}", nTH + 1, Fermat(nTH));
            Console.WriteLine(s);
        }
    }
}
