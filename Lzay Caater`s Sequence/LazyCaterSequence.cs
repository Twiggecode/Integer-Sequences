namespace DefaultNamespace
{
    public static class LazyCaterSequence
    {
        public static int CalculateLazyCaterSequence(int n)
        {
            if(n == 0)
            {
                return 1;
            }

            //formula is p = (n^2 + n + 2) / 2. Easy~
            return ((n * n + n + 2) / 2);
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

                    if (nTH < 0)
                    {
                        throw new Exception("s");
                    }

                    Console.WriteLine(CalculateLazyCaterSequence(nTH));
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