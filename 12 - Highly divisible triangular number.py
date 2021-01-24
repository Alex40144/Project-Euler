import math
import time
def factors(num):
    count = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            count +=1
    return count * 2

start = time.time()
value = 1
while True:
    total = 0
    for i in range(1, value+1):
        total += i
    if factors(total) > 500:
        print(total)
        break
    value += 1

finish = time.time() - start
print(f"finished in {finish} ms")