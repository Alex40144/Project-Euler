import time
start = time.time()

def factor(num):
    #returns a list of factors.
    factors = []
    for i in range(1,num):
        if num % i == 0:
            factors.append(i)
    sum = 0
    for i in range(0,len(factors)):
        sum += factors[i]
    return sum

ans=[]
for i in range(1,10000):
    ans.append(factor(i))

for i in range(1,10000):
    if i in ans:
        pos = ans.index(i)
        if pos == factor(i):
            print("yes")
print(f"finished in {time.time() - start} s")