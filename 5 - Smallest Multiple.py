num = 0
def test(val):
    if val == 0:
        return False
    for i in range(1,20):
        if num % i != 0:
            return False
    return True

while True:
    if test(num):
        print(num)
        break
    else:
        num += 20
    