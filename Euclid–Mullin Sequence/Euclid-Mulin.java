public static int smallPrimeFactor(n)
{
    for (i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return i;
        }
    }

    return n
}

public static int EuclidMullin(n)
{
    product = 1

    for (i = 0; i < n; i++)
    {
        ans = smallPrimeFactor(product + 1)
        product *= ans
    }

    return ans
}