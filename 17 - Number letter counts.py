import time
start = time.time()


total_letters = 0
for number in range(0,1000):
    number = '{0:03}'.format(number)
    words = ""
    letters=0
    chars = [int(d) for d in str(number)]
    if chars[0] == 1:
        words = words + "one"
    if chars[0] == 2:
        words = words + "two"
    if chars[0] == 3:
        words = words + "three"
    if chars[0] == 4:
        words = words + "four"
    if chars[0] == 5:
        words = words + "five"
    if chars[0] == 6:
        words = words + "six"
    if chars[0] == 7:
        words = words + "seven"
    if chars[0] == 8:
        words = words + "eight"
    if chars[0] == 9:
        words = words + "nine"
    if chars[0] != 0:
        if chars[1] == 0 and chars[2] == 0:
            words = words + " hundred"
        else:
            words = words + " hundred and "

    if chars[1] == 1:
        if chars[2] == 0:
            words = words + "ten"
        if chars[2] == 1:
            words = words + "eleven"
        if chars[2] == 2:
            words = words + "twelve"
        if chars[2] == 3:
            words = words + "thirteen"
        if chars[2] == 4:
            words = words + "fourteen"
        if chars[2] == 5:
            words = words + "fifteen"
        if chars[2] == 6:
            words = words + "sixteen"
        if chars[2] == 7:
            words = words + "seventeen"
        if chars[2] == 8:
            words = words + "eighteen"
        if chars[2] == 9:
            words = words + "nineteen"
    else:
        if chars[1] == 2:
            words = words + "twenty "
        if chars[1] == 3:
            words = words + "thirty "
        if chars[1] == 4:
            words = words + "forty "
        if chars[1] == 5:
            words = words + "fifty "
        if chars[1] == 6:
            words = words + "sixty "
        if chars[1] == 7:
            words = words + "seventy "
        if chars[1] == 8:
            words = words + "eighty "
        if chars[1] == 9:
            words = words + "ninety "

        if chars[2] == 1:
            words = words + "one"
        if chars[2] == 2:
            words = words + "two"
        if chars[2] == 3:
            words = words + "three"
        if chars[2] == 4:
            words = words + "four"
        if chars[2] == 5:
            words = words + "five"
        if chars[2] == 6:
            words = words + "six"
        if chars[2] == 7:
            words = words + "seven"
        if chars[2] == 8:
            words = words + "eight"
        if chars[2] == 9:
            words = words + "nine"
    for i in range(0, len(words)):
        if words[i] != " ":
            letters +=1
    total_letters += letters
### one thousand
total_letters += 11
print(total_letters)
print(f"finished in {time.time() - start} s")