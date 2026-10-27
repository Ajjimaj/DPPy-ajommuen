#!/usr/bin/env python3

"""
x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))

print("Thank you!")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{x} * {y} = {x * y}")
"""

# function
def calculate():
        x = int(input("Give me the first number: "))
        y = int(input("Give me the second number: "))

        print("Thank you!")
        print(f"{x} + {y} = {x + y}")
        print(f"{x} - {y} = {x - y}")
        print(f"{x} / {y} = {x / y:.2f}")
        print(f"{x} * {y} = {x * y}")

# __name__ == dunder name (ดันเดอร์ เนม)
# ถ้า if __name__ == "__main__": เป็น จริง (True) ทำให้ฟังก์ชัน calculate() ถูกเรียกใช้งาน

if __name__ == "__main__":
    # function call
    calculate()
