import time
start = time.time()

total = 1
number = 100
for i in range(number, 0, -1):
    total *= i
digit_sum = 0
chars = [int(d) for d in str(total)]
for i in range(0, len(chars)):
    digit_sum += chars[i]
print(digit_sum)

print(f"finished in {time.time() - start} s")