from fractions import Fraction as Fr

'''
Example:

n	fraction	decimal
0	1	        +1.000000000
1	±1/2	        ±0.500000000
2	1/6	        +0.166666666
3	0	        +0.000000000
4	−1/30	        −0.033333333
5	0	        +0.000000000
6	1/42	        +0.023809523
7	0	        +0.000000000
8	−1/30	        −0.033333333
9	0	        +0.000000000
10	5/66	        +0.075757575
11	0	        +0.000000000
12	−691/2730	−0.253113553
13	0	        +0.000000000
14	7/6	        +1.166666666
15	0	        +0.000000000
16	−3617/510	−7.092156862
17	0	        +0.000000000
18	43867/798	+54.97117794
19	0	        +0.000000000
20	−174611/330	−529.1242424
'''

def Bernoulli(n):
        A = [0] * (n+1)
        for m in range(n+1):
                A[m] = Fr(1, m+1)
                for j in range(m, 0, -1):
                        A[j-1] = j*(A[j-1] - A[j])
        return A[0]


find_val = int(input("Enter the nth value to find : "))
bn = [(i, Bernoulli(i)) for i in range(100)]
width = max(len(str(b.numerator)) for i,b in bn)
print(bn[find_val][1].numerator)
