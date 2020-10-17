for a in range(500):
    for b in range(500):
        for c in range(500):
            if a**2 + b**2 == c**2:
                print(a)
                print(b)
                print(c)
                if a+b+c == 1000:
                    print("================")
                    print(a*b*c)
                    exit()