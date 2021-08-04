""" Catalan Numbers (sequence A000108 in the OEIS) """
""" (2n)! / ((n + 1)!n!) """
# The first ten  (starting with n=0 are: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862)

# A recursive function to
# find nth catalan number
def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum
	# of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n-i-1)

	return res



for i in range(10):
	print(catalan(i))
