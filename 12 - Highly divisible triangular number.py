def devisors(num):
    count = 0
    for i in range(1,num):
        if num % i == 0:
            count +=1
    return count


value = 1
while True:
    total = 0
    for i in range(0, value):
        total += i
    if devisors(total) > 500:
        print(total)
        break
    value += 1
