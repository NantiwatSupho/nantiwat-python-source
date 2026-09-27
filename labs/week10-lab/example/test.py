# 1.รับค่า text จากผู้ใช้
# 2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3.แสดงผลจำนวนอักขระในข้อความ text

# ตัวอย่างหน้าจอ
# Insert your text: Boonchoo Jitnupong
# charater to find: o
# 5 letters 'o' found in 'Boonchoo Jitnupong'

print("\n=== ITERATING THROUGH STRING ===")
count = 0

text = input("Insert your text :")
char = input("charater to find :")
for i in text:
    if i == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  # True
print("'at' not in 'battle':", 'f' not in 'battle')  # False

print("Path: C:\\Users\\Python")

text = "welcome to the world of python"

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}") #Upper: WELCOME TO THE WORLD OF PYTHON
print(f"Lower: {text.lower()}") # Lower: welcome to the world of python
print(f"Title: {text.title()}") # Title: Welcome To The World Of Python
print(f"Capitalize: {text.capitalize()}") #Capitalize: Welcome to the world of python


# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ storng password คือ ยาวมากกว่า 8 ตัว, มีตัวอักษร @ 1 ตัว, มีตัวเลข, มีตัวอักษร
#
# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not storng!
#
# Insert your password: Test@123
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum() 
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left and right:
    print("Your password is strong!")
else:
    print("Your password is not strong!")
