public static int factorial(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }

    if (n < 0)
    {
        System.out.println("Negative Integer is not allowed");
    }

    return n * factorial(n - 1);
}
}