# แบบที่ 1
# การ import ไฟล์ อื่นเข้ามา
import util.number

print(util.number.factorial(5))
print(util.number.factorial(10))
print(util.number.fibonacci(5))


# แบบที่ 2
# การ import และใช้นามแฝง
import util.number as nb

print(nb.factorial(5))
print(nb.factorial(10))
print(nb.fibonacci(5))


# แบบที่ 3
# การ import แบบเลือกมาบางฟังก์ชัน
from util.number import factorial as ft, fibonacci as fb

print(ft(5))
print(ft(10))
print(fb(100))

from util.number import *

print(factorial(5))
print(factorial(10))
print(fibonacci(5))