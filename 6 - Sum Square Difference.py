square_sum = 0
add_sum = 0

for i in range(1,101):
    square_sum += i*i

for i in range(1,101):
    add_sum += i

add_sum = add_sum*add_sum

print(add_sum-square_sum)