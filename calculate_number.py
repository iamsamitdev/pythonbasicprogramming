try:
    result = 0
    number1 = float(input("Enter nubmer 1: "))
    number2 = float(input("Enter nubmer 2: "))
    result = number1 / number2
    print("ผลหารที่ได้คือ ", result)
except ValueError:
    print("คุณป้อนข้อมูลไม่ถูกต้อง")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วย 0 ได้")
