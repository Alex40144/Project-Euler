Fibonacci = [1,2]
sum = 0
while Fibonacci[-1] < 4000000:
    Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])

for i in range(len(Fibonacci)):
    if Fibonacci[i] % 2 == 0:
        sum += Fibonacci[i]

print(sum)