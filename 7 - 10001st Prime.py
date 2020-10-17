def prime(val):
    for i in range(2,val):
        if val % i == 0:
            return False
    return True


count=0
val = 1
while count <= 10001:
    if prime(val):
        print(f"{count}  |  {val}")
        count += 1
    val += 1