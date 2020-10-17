import time, math
start_time = time.time()

def test(val):
    for i in range(2,int(math.sqrt(val))+1):
        if val % i == 0:
            return False
    return True

prime = 0
number = 5
totalprime = 5
while prime < 1999999:
    if test(number) == True:
        prime = number
        totalprime += prime
    number += 2

print(totalprime)
print("--- %s seconds ---" % (time.time() - start_time))