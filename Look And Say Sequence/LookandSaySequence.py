################################
## Look and Say Sequence      ##
################################

#Idea : Every current term is dependent on previous term
#Example : 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
#For 1, it is "1"
#For 2, we see previous term and so it is 1(count) "1"(Ones) => "11"
#For 3, we see previous term and so it is 2(count) "1"(Ones) => "21"
#For 4, we see previous term and so it is 1(count) "2"(two)
#and 1(count) "1"(ones) => "1211"

def seq(n):
        if(n == 1):
                return "1"
        if(n == 2):
                return "11"
        s = "11"
        for i in range(3, n+1):
                s += "$"
                l = len(s)
                count = 1
                tmp = ""
                for j in range(1, l):
                        if(s[j] != s[j-1]):
                                tmp += str(count + 0)
                                tmp += s[j-1]
                                count = 1
                        else:
                                count += 1
                s = tmp
        return s

find_val = int(input("Enter the nth value to find : "))
print(find_val, "th value in Look and Say Sequence is ", seq(find_val))
