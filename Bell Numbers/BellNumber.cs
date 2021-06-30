namespace DefaultNamespace
{
    public class BellNumber
    {
        private static int CalculateNthBellNumber(int n)
        {
            // create 2d array to store Bell triangle
            int[,] bellArray = new int[n, n];

            if(n == 0 || n == 1)
            {
                return 1;
            }
            // arbitrary insert first bell number
            bellArray[0, 0] = 1;

            for(int i = 1; i < n; i++)
            {
                // first number in row i is the last number in row i-1;
                bellArray[i, 0] = bellArray[i - 1, i - 1];

                for(int j = 1; j<= i; j++)
                {
                    // last number + the number at the same solumn but previous row
                    bellArray[i, j] = bellArray[i, j - 1] + bellArray[i - 1, j - 1];
                }
            }

            // last number at last row is the number you want
            return bellArray[bellArray.GetLength(0) - 1, n - 1];


        }

        public static void Run()
        {
            int nTH;

            Console.WriteLine("Please enter a integer");
            while (true)
            {
                string input = Console.ReadLine();

                try
                {
                    nTH = Convert.ToInt32(input);

                    if(nTH < 0)
                    {
                        throw new Exception("The number cannot be less than 0");
                    }

                    Console.WriteLine(CalculateNthBellNumber(nTH));
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Invalid, please enter an valid number");
                    Console.WriteLine(e);
                }
            }
        }
    }
    }
}