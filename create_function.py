# ตัวอย่างการสร้างฟังก์ชัน
def hello():
    print("Hello Python")


# ฟังกชันมีการรับค่ารับเข้าไป
def sayhello(name):
    print("Hello ", name)


# ฟังก์ชันแบบมีการ Return ค่า
def area(width, height):
    return width * height


# ฟังก์ชันที่มีค่าเริ่มต้นของ Argument
def show_info(name="", salary=0, lang=""):
    return [name, salary, lang]


# เรียกใช้งานฟังก์ชัน (Call function)
hello()
sayhello("Samit")
print("พื้นที่คือ ", area(10, 20))
print("พื้นที่คือ ", area(5, 3))
show_info()
print(show_info("Samit Koyom")[0])
print(show_info("Samit", 30000, "Python")[0],"\n",
        show_info("Samit", 30000, "Python")[1],"\n",
        show_info("Samit", 30000, "Python")[2])