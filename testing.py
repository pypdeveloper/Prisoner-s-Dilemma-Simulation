import random

n = 0

while n < 100:
    true = random.choices([True, False], weights=(10,90))
    print(true)
    if true[0] == False:
        print(False)
    else:
        print(True)
    if n == 100:
        break
    n += 1