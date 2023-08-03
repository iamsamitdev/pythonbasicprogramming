numbers = {1, 12, -10, 7, 5}
names = {"Samit", "Apiwat", "Wichai"}

#  ตัวแปรแบบ set จะไม่ดึงสมาชิกที่ซ้ำออกมา
print(numbers)
print(names)

# loop สมาชิก
for n in names:
    print(n)

# เพิ่มสมาชิกใหม่
numbers.add(20)
print(numbers)
