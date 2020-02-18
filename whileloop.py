n = 1

# normal loop
while n <= 500:
    if n == 201:
        break
    else:
        if n % 10 == 0:
            print("%03d" % n)
        else:
            print("%03d" % n, end=" ")
        n = n + 1

# Infinity Loop
while True:
    print(n)
    n = n + 1
