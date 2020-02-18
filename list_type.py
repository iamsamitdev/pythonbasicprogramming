# การสร้างข้อมูลแบบ List ใน Python
numbers = [1, 5, 7, 12, -10]  # สร้าง list เก็บข้อมูล integer
persons_name = ['John', "Joey", "Jack", "Joy"] # เก็บ String
profile = ["Wichai", 30, "Male", "Programmer", 165.50, True]  # เก็บผสมกัน

print(numbers)
print(persons_name)
print(profile)

# ดึงสมาชิกโดยระบุ Index (ลำดับที่)
print(numbers[0])
print(persons_name[3])
print(profile[-2])

# อ่านค่าสมาชิกโดยการวนลูป
for p in persons_name:
    print(p)

sum_data = 0
for n in numbers:
    sum_data += n

print(sum_data)

# การสร้าง list แบบว่าง
product_name = []

# การเพิ่มสมาชิกเข้าไปใน list ว่าง
product_name.append("Apple")
product_name.append("Mango")
product_name.append("Grape")
print(product_name)

# การเปลี่ยนข้อมูลสมาชิก
product_name[1] = "Banana"
print(product_name)

# การลบสมาชิกออกจาก list
product_name.pop(2)
print(product_name)

# การนับจำนวนสมาชิกใน list
print(len(product_name))
print(len(numbers))

