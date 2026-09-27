'''
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัวได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
    ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
    ผู้ใช้เลือกตัวดำเนินการอื่นนอกจาก + - * / raise ValueError
    ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
    โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

    ตัวอย่างที่ 1: 10
    ตัวอย่างที่ 2: 0
    เครื่องหมาย (+,-,*,/):

    ไม่สามารถหารด้วยศูนย์ได้
    จบการทำงาน

'''

try:
    num1 = float(input("ตัวเลขที่ 1:"))
    num2 = float(input("ตัวเลขที่ 2:"))
    operator = input("ครื่องหมาย (+,-,*,/):")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")
    
    print(f"{num1} {operator} {num2} = {result}")

except ValueError: #กรณีผู้ใช้ไม่พิมพ์ตัวเลข
    print("กรุณากรอกข้อมูลที่เป็นตัวเลข")
except ZeroDivisionError: #กรณีผู้ใช้ใส่ตัวหารเป็น 0
    print("ไม่สามารถหารด้วยศูนย์ได้")
except Exception: #กรณีอื่นๆ
    print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจว่าคืออะไร")
else :#จะทำที่นี่ก็ต่อเมื่อไม่มี exception
    print("คำนวณข้อมูลเรียบร้อยแล้ว")
finally: #ทำเสมอไม่ว่าจะมีหรือไม่มี exception เกิดขึ้นก็ตา
    print("จบการทำงาน")