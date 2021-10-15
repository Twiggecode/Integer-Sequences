# Markov Numbers

seed = (1,2,5)
markov = set()
markov.add(1)
queue = []
queue.append(seed)

n = int(input('Enter n: '))
seq = open('markov_sequence.txt', 'w')
while len(markov) <= n**3:
    curr = queue.pop()
    p,q,r = (curr)
    markov.add(p)
    markov.add(q)
    markov.add(r)
    left = (p,r,3*p*r-q)
    right = (q,r,3*q*r-p)
    queue.insert(0,left)
    queue.insert(0,right)
markov = list(markov)
markov.sort()
for i in range(0, n+1): 
    seq.write(f'{i}th element: {markov[i]}\n')
print(markov[n])
    
