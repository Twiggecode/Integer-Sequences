#A program to find the nth number in the Golomb sequence.
#https://en.wikipedia.org/wiki/Golomb_sequence

def golomb(n):
    n=int(n)
    if n==1:return 1
    #Set up a list of the first few Golomb numbers to "prime" the function so to speak.
    temp=[1,2,2,3,3]
    #We will be modifying the list, so we will use a while loop to continually check if we can get the nth number yet.
    while len(temp)<n:
        #Here comes the fun part. Starting with 0, we loop through every number (i) lower than n to build the Golomb list as much as we need.
        for i in range(n):
            #If the list is longer than (i), we skip it.
            if len(temp)>i:continue
            #If the list ISN'T longer than (i), which it shouldn't be, we do some stuff.
            else:
                #We set a variable for the final value in the list, so we can increment it as we go.
                lastval=temp[-1]
                #We grab the number at the lastval index in the list, and set that to be our range.
                #We add lastval+1 (the next element in the sequence) to the list (range) times, and then move to the next (i)
                for x in range(temp[lastval]):
                    temp.append(lastval+1)
    #Once we have extended the list to or beyond the length of n, we can now grab the number in position n in the list!
    return (temp[n-1])
print(golomb(input('Enter n> ')))