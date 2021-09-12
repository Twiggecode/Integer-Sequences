def natural_numbers(start,end):
    if start<=0 or end<=0:
        print("A Natural Number can't be negative or equal to zero..")
    elif end<start:
        print('End Number should be larger than starting number')
    
    else:
        for i in range(start,end+1):
            print(i,end=" ")

def main():
    try:
        start=int(input("Enter your starting number  : "))
        end=int(input("Enter your end number  : "))
        natural_numbers(start,end)
    except ValueError:
        print("A natural number can't be fractional")


if __name__=='__main__':
    main()