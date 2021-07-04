import math

# Taking user imput
def user_input():
	n = int(input("Enter n: "))
	return n

# Find required number in a power series
def find_power_of2():
	n = user_input()
	
	while True:
		if (n > -1):
			break
		print("Invalid input, please enter a positive number or 0.")

	number = math.pow(2, n)
	return int(number)


# Main program
if __name__ == '__main__':
	print(f'The nth term in the sequence is {find_power_of2()}')
