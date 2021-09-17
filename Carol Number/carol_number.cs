using System;

namespace IntegerSequences.CarolNumbers
{
    class carol_number
    {
        // The first few Carol numbers are: −1, 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527 (sequence A093112 in the OEIS).
        private static double carolNumber(int n)
        {
            n++;
            return (Math.Pow(Math.Pow(2, n) - 1, 2)) - 2;
        }


        public static void Main(string[] args)
        {
            Console.WriteLine("Please, enter an integer: ");
            string input = Console.ReadLine();
            int nTH = int.Parse(input);

            Console.WriteLine(carolNumber(nTH));
        }
    }
}
