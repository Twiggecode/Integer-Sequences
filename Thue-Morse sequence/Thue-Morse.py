"""
parameter: integer n: index of ThueMorse sequence
returns value of sequence at index n

count number of 1s in binary representation n
if number of 1s is even -> value at index is 0
else -> value at index is 1
n:     0,1,2,3,4,5
value: 0,1,1,0,1,0
"""
def ThueMorse(n):
  n_bin = "{0:b}".format(n)

  one_count = 0
  for bit in n_bin:
    if bit == '1':
      one_count += 1
  
  if one_count % 2 == 1:
    return 1
  return 0


#Driver Code
if __name__ == "__main__":

  n = int(input("Enter index of value to find: "))

  print(ThueMorse(n))
