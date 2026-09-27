'''
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน
fnction convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่เขียนด้วย
'''

def convert_currency(a,b):
    if b == "USD":
        print(f"{a} THB = {a / 32.0} USD")
    else:
        print(a, "USD = ", a * 32.0, "THB")

convert_currency(100,"USD")
convert_currency(100,"THB")

