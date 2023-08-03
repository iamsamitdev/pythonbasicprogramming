from tkinter import *
from tkinter import ttk
import sqlite3

def con_db():
    return sqlite3.connect('db/companydb.db')


# ฟังก์ชันให้แสดงผลข้อมูลจากตาราง teachers
def insertDataToTreeView():
    # ลบข้อมูลออกจาก Treeview widgit
    for c in viewTcr.get_children():
        viewTcr.delete(c)

    con_db()  # เรียกใช้งานฟังก์ชันเชื่อมต่อฐานข้อมูล
    cs = con_db().cursor()
    cs.execute("select * from employee")# ใช้คำสั่ง select ดึงข้อมูลจากตาราง employee
    data = cs.fetchall()  # แสดงผลข้อมูลทั้งหมดในตาราง employee
    # อ่านข้อมูลและเพิ่มข้อมูลไปยัง Treeview widget ทีละแถว
    for d in data:
        viewTcr.insert("", "end", values=d)


mainFrm  = Tk()
mainFrm.withdraw()  # เมื่อหน้าจอขึ้นมา หน้าจอหลักจะถูกปิด

# คำสั่งสร้าง Treeview widget
frmTeacher = Toplevel()    # กำหนดให้ปรากฏขึ้นมาเป็นหน้าต่างบนสุด
frmTeacher.title("รายชื่อพนักงาน") # แสดงข้อความที่ title bar
ttk.Frame(frmTeacher, height=220, width=750).pack() # กำหนดขนาด Treeview widget
frmTeacher.resizable(width=0, height=0) # กำหนดไม่ให้สามารถปรับขนาดได้

# กำหนดขนาดและจำนวนคอลัมน์ Treeview widget
viewTcr = ttk.Treeview(frmTeacher, column=("id", "fullname", "email", "salary"), show="headings")
viewTcr.place(height=200, width=720, x=10, y=10)

# กำหนดให้แสดง scrollbar
sc = ttk.Scrollbar(frmTeacher, orient="vertical",command=viewTcr.yview)
sc.place(height=200, x=720, y=200)  # กำหนดความยาวและตำแหน่ง scrollbar
viewTcr.configure(yscrollcommand=sc.set)

# กำหนดขนาดความกว้างของคอลัมน์ Treeview widget
viewTcr.column("#1", width="80")
viewTcr.column("#2", width="150")
viewTcr.column("#3", width="150")
viewTcr.column("#4", width="200")

# กำหนดที่หัวแต่ละคอลัมน์
viewTcr.heading("#1", text="ลำดับ")
viewTcr.heading("#2", text="ชื่อ-สกุล")
viewTcr.heading("#3", text="อีเมล์")
viewTcr.heading("#4", text="เงินเดือน")

# เรียกใช้ฟังก์ชันแสดงข้อมูลใน TreeView widget ทันทีเมื่อแสดงผลหน้าต่าง employee
insertDataToTreeView()

mainFrm.mainloop()