###################################
###     Pronic Numbers          ###
###################################

#Pronic Series Formula 2t(n) = n(n+1) where n>=0
#Example: {0,2,6,12,20,30,42,56,72,90....}

find_val = int(input("Enter the Nth Value : "))
check = 0
ans = 0
iterator = 1
while(check != find_val):
        flag = False
        #Validating Whether the range has any Pronic Number
        for i in range(0,iterator+1):
                if(i*(i+1) == iterator):
                        flag = True
                        break
        if(flag):
                #Updating the answer and incrementing check
                #for outer while loop
                check += 1
                ans = iterator
        iterator += 1
        
print(find_val, "th Pronic Number is ", ans)
