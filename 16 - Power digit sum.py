for n in range(0,1000):
    chars = [int(i) for i in str(n)]
    for i in range (0,len(chars)):
        total += chars[i]
    print(total)