using System;

namespace DefaultNamespace
{
    public class EuclidNumber
    {
        public static bool IsPrime(int num)
        {
            if (num <= 1) return false;
            if (num == 2) return true;
            if (num % 2 == 0) return false;

            /*consists of dividing n by each integer m that is greater than 1 
             * and less than or equal to the square root of n.
             * If the result of any of these divisions is an integer, 
             * then n is not a prime, otherwise it is a prime. 
             * Indeed, if n = a*b is composite (with a and b ≠ 0)
             * then one of the factors a or b is necessarily at most square root of n
            **/
            int boundary = (int)Math.Floor(Math.Sqrt(num));

            for (int i = 3; i <= boundary; i+=2)
            {
                if (num % i ==0)
                {
                    return false;
                }
            }
            return true;
        }

        public static double calculateNthEuclidNumber(int n)
        {
            // the first euclis number
            double num = 3;
            int count = 0;
            
            if(n == 0)
            {
                // the first euclid number is 2 + 1
                return 3;
            }


            for(int i = 3; i < int.MaxValue; i++)
            {
                if (IsPrime(i))
                {
                    // current prime number multiples last euclid number - 1
                    num = (i * (num - 1)) + 1;
                    count++;
                }

                if(count == n)
                {
                    return num;
                }
            }
            return num;
        }
        static void Main(string[] args)
        {
            int nTH;
            
            Console.WriteLine("Please enter a integer");
            while (true)
            {
                string input = Console.ReadLine();

                try
                {
                    nTH = Convert.ToInt32(input);
                    Console.WriteLine(calculateNthEuclidNumber(nTH));
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Invalid, please enter an valid number");
                }
            }
        }
    }
}