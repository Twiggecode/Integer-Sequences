# This Algorithm prints all prime numbers based on user input.
# Requesting user input for starting Number and ending Number
start = int(input("Enter starting number: "))
end = int(input("Enter end number: "))

# For loop to loop through numbers from the inputted start and end numbers
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
