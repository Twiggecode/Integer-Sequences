function factorial(n)
{
    if (n < 0) { 
      console.error('Negative integer not permitted');
      return 0;
    } else if (n < 3) {
      return n;
    }

    return n * factorial(n - 1);
};
