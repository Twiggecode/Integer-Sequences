
import java.util.*;
class GFG
{
static ArrayList<Integer> factors(int n)
{
    // ArrayList to store the factors
    ArrayList<Integer> v = new ArrayList<Integer>();
    v.add(1);
 
    for (int i = 2;
             i <= Math.sqrt(n); i++)
    {
        if (n % i == 0)
        {
            v.add(i);
            if (n / i != i)
            {
                v.add(n / i);
            }
        }
    }
    return v;
}
static boolean checkAbundant(int n)
{
    ArrayList<Integer> v;
 
    int sum = 0;
    v = factors(n);
    for (int i = 0; i < v.size(); i++)
    {
        sum += v.get(i);
    }
    if (sum > n)
        return true;
    else
        return false;
}

static boolean checkSemiPerfect(int n)
{
    ArrayList<Integer> v;
    v = factors(n);
    // sorting the ArrayList
    Collections.sort(v);
 
    int r = v.size();
 
    boolean subset[][] = new boolean[r + 1][n + 1];
 
    for (int i = 0; i <= r; i++)
        subset[i][0] = true;

    for (int i = 1; i <= n; i++)
        subset[0][i] = false;

    for (int i = 1; i <= r; i++)
    {
        for (int j = 1; j <= n; j++)
        {

            if (j < v.get(i - 1))
                subset[i][j] = subset[i - 1][j];
            else {
                subset[i][j] = subset[i - 1][j] ||
                               subset[i - 1][j -
                                v.get(i - 1)];
            }
        }
    }

    if ((subset[r][n]) == false)
        return false;
    else
        return true;
}
 
// Function to check  weird or not
static boolean checkweird(int n)
{
    if (checkAbundant(n) == true &&
        checkSemiPerfect(n) == false)
        return true;
    else
        return false;
}
 

public static void main(String args[])
{
    int n = 7;
 
    if (checkweird(n))
        System.out.println("It is a Weird Number");
    else
        System.out.println("It is not a Weird Number");
}
}
