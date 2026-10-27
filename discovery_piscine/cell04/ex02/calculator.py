#!/usr/bin/env python3

x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))

result_1 = x + y
result_2 = x - y
result_3 = x * y
result_4 = x / y

print("Thank you!")
print(f"{x} + {y} = {result_1}")
print(f"{x} - {y} = {result_2}")
print(f"{x} x {y} = {result_3}")
print(f"{x} / {y} = {result_4:.2f}")
