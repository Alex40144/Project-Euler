import time
start = time.time()
count = 0
Fibonacci = [1,2]
while len(str(Fibonacci[-1])) < 1000:
    Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
    count +=1
print(count + 3) # because we already have the first 2 and we need the first one to exceed 1000 chars
#probably should change the condition on the for loop to be !> 1000
print(f"finished in {time.time() - start} s")