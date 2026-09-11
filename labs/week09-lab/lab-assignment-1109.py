'''
สร้างไฟล์ใหม่ใน FOLDER /assigments/week09/lab-assignment-1109.y

เครื่องคำนวณค่าไฟฟ้าแบบขั้นบรรไดเขียนโปรแกรมคำนวณค่าไฟฟ้าจากจำนวนหน่วยไฟฟ้าที่ใช้ในเดือนนั้น โดยใช้ฟังก์ขัน
calculate_electricity_cost(units)

ค่าไฟฟ้าขึ้นอยู่กับปริมาณการใช้งาน
จำนวนหน่วยที่ใช้     อัตราต่อหน่วย
1-50 หน่วยแรก         2.50 บาท
51-100               3.00
101-200              3.50
>200                 4.00


'''

def calculate_electricity_cost(units):
    print("รายละเอียดค่าไฟ")
    if units <= 0:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
    if units <= 50:
        cost = (units * 2.50) + 25
        print(f"{units} หน่วย: {2.50 * units} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print("รวมค่าไฟทั้งสิน:" , cost)
    elif units <= 100:
        cost = (2.50*50)  + ((units - 50) * 3.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print(f"51-{units} หน่วย: {(units - 50) * 3.00} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print("รวมค่าไฟทั้งสิน:" , cost)
    elif units <=200:
        cost = (2.50 * 50) + (3.00 * 50) + ((units - 100) * 3.50) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print(f"101-{units} หน่วย: {(units - 100) * 3.50} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print("รวมค่าไฟทั้งสิน:" , cost)
    elif units >200:
        cost = (2.50 * 50) + (3.00 * 50) + (100 * 3.50) + ((units - 200) * 4.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print("101-200 หน่วย: 350.00 บาท")
        print(f"201-{units} หน่วย: {(units - 200) * 4.00} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print("รวมค่าไฟทั้งสิน:" , cost)
while True:
    print( "==== โปรแกรมคำนวณค่าไฟฟ้า ====" )
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู:")
    if choice == '1':
        units = float(input("กรอกจำนวนหน่วยไฟฟ้า:"))
        calculate_electricity_cost(units)
    elif choice == '2':
        break
    else:
        print("ไม่พบข้อมูล")