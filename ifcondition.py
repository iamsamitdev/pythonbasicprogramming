n = 10
p = 20
status = True

# if
if n == 10:
    print('n is 10')

# if...else
if n >= p:
    print('n larger than p')
else:
    print('n less than p')

# if...else
if status:
    print('Status Correct')
else:
    print('Status False')

# if ... else
if n >= 10 and p <= 30:
    print("Data approve")
else:
    print("Incorrect")

# if..elif...else
if n == 10:
    print("n is 10")
elif n == 20:
    print("n is 20")
elif n == 30:
    print("n is 30")
else:
    print('Invalid number')

# if ซ้อน if (nested if..else)
if status:
    if n == 10:
        if p >= 20:
            print("Correct Value")
else:
    print("Status fail!")