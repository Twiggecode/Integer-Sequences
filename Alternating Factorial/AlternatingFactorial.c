// TODO: Try ints, longs and convert to floats
/**
 * af(n) = SIGMA i=0 to n, (-1)^(n-i)i!
 * af(n) = n! - af(n - 1), which af(1) = 1
 *
 */
#include <math.h>
#include <stdio.h>

float factorial(float);
// float sigma(float);

int main() {

    float n = 3.0;
    float i = 0.0;
    float negOne = -1.0;
    float ans;


    while (i <= n) {
        float m = n - i;
        float equals = pow(negOne, m);
        float fact = factorial(i);
        ans = equals * fact;
        ++i;
    }

    printf("%f\n", ans);

    return 0;
}

float factorial(float n) {
    return (n == 0) ? 1 : (n * factorial(n - 1));
}

// float sigma(float n) {
//     float i = 0;
//     float equals;
//     while (i <= n) {
//         float m = (n - i);
//         equals = pow(-1.0, m) * factorial(i);
//         --i;
//     }
//
//     return equals;
// }
