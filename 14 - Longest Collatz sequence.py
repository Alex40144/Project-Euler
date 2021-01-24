max = 0
for start in range(1, 1000000):
    sequence = [start]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1]/2)
        else:
            sequence.append(3*sequence[-1]+1)
    if len(sequence) > max:
        max = len(sequence)
        max_start = start

print(max)
print(max_start)