# Lazy caterer's sequence 

# describes the maximum number of pieces a circular pizza
# can be divided into with an increasing number of cuts,n.
# recursive formula is f(n) = f(n-1) + n


def f(seq):
  seq.append(seq[-1] + k)
  
  
if __name__ == '__main__':

  seq = [1]     # f(0) = 1
  
  MAX = 10000
  
  n = int(input())
  
  for k in range(MAX): # prints sequence upto input n 
    f(seq)
    
  print(seq)
  
