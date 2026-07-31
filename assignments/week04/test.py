# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i, o, u)
# โดยต้องใช้ loop-for ด้วย เท่านั้น

# ตัวอย่างหน้าจอ
# What is your name?: Boonchoo
# Your text have 4 vowels.

name = input("Enter your name: ")
count = 0
for letter in name:
    if letter == 'a' or letter == 'A':
        count += 1
    if letter == 'e' or letter == 'E':
        count += 1
    if letter == 'i' or letter == 'I':
        count += 1
    if letter == 'o' or letter == 'O':
        count += 1
    if letter == 'u' or letter == 'U':
        count += 1

print(f"Your text has {count} vowels")
