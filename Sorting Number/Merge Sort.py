# done recursively, using divide and conquer strategy
# the function does in an inplace sort, hence there is no need for a return value
def mergesort(nlist):
    if len(nlist) > 1: # checks if the length of list is greater than 1
        mid = len(nlist)//2 # identify the middle element for the split
        llist = nlist[:mid]
        rlist = nlist[mid:]

        mergesort(llist) # call merger sort recursively on the split lists
        mergesort(rlist)
        i=j=k=0
        while i < len(llist) and j < len(rlist): # check if the counter has not exceeded the length of the lists
            if llist[i] < rlist[j]: # compare the values between the 2 lists
                nlist[k] = llist[i] # append or add smaller value to new list
                i+=1
            else:
                nlist[k] = rlist[j]
                j+=1
            k+=1
        while i < len(llist): # add all remaining elements in left list to resultant list
            nlist[k] = llist[i] 
            k+=1
            i+=1
        while j < len(rlist): # add all remaining elements in right list to resultatnt list
            nlist[k] = rlist[j]
            k+=1
            j+=1
    else:
        nlist = nlist # if lenght of list is less than 1
