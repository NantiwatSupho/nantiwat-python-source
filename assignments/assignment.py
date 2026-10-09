def deposit(money):
    balance = 1000
    print("ยอดเงินเริ่มต้น:", balance, "บาท")
    try:
        amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
        balance += amount
    except ValueError as e:
        print("เกิดข้อผิดพลาด: ", e)
    else:
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
deposit(0)