
def is_palindrome(num):
    reverse = int(str(num)[::-1])
    if reverse == num:
        return True
    else:
        return False

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            if i*j > max:
                max = i*j

print(max)