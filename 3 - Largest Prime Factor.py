import math
givenValue = 600851475143

def prime(val):
    for i in range(2,val):
        if val % i == 0:
            return False
    return True

for i in range(int(math.sqrt(givenValue)), 0 , -1):
    if givenValue % i == 0:
        if prime(i):
            print(f"largest prime: {i}")
            break