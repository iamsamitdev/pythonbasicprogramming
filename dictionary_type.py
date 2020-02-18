numbers = {1: "One", 2: "Two", 3: "Three"}

people = {
                 1: {'name': 'John', 'age': '27', 'sex': 'Male'},
                 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
}

print(people[1]['name'])

print(numbers)

# การอ่านสมาชิกของ dictionary
print(numbers[2])

# การอ่านคียร์ทั้งหมดออกมา
print(numbers.keys())

# การอ่าน value ออกมา
print((numbers.values()))

# การลูปอ่านสมาชิกทั้งหมดของ dictionary
for k, v in numbers.items():
    print(k, v)

for v in numbers.values():
    print(v)

for k in numbers.keys():
    print(k)

# การเพิ่มค่าใหม่เข้าไปใน dictionary
numbers[4] = "Four"
print(numbers)

# แก้ไขสมาชิกของ dictionary
numbers[2] = "TwoUpdate"
print(numbers)

# การลบสมาชิกออก
numbers.pop(2)
print(numbers)