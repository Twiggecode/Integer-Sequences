public static int pell_numbers(int n)
{
    if (n <= 2)
    {
        return n;
    }
    
    int first = 1;
    int second = 2;

    for (int i = 3; i < n + 1; i++)
    {
        int temp = 2 * second + first;
        first = second;
		second = temp;
    }

    return second;
}