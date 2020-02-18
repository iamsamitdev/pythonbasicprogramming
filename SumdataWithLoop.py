sum_data = 0
count = 1
while True:
    number = input("Enter your number  %d: " % count)
    if number == "exit":
        print("Exit program")
        print("Summary data = ", sum_data)
        break
    else:
        sum_data += int(number)
    count = count + 1
