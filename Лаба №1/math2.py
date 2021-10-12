# mama-ya-matematik-26

import math as m
import random

print("z = (2*m.tan(x)-m.sqrt(x))/x")
while True:
  try:
    x = float(input("x = "))
    z = (2*m.tan(x)-m.sqrt(x))/x
    print("z =", z)
    break
  except ValueError:
    print("Print number")
  except ZeroDivisionError:
    print("Division by zero")

print("Знайти усі кратні 3 числа від x до y")
while True:
  try:
    x = int(input("x: "))
    y = int(input("y: "))
    break
  except ValueError:
    print("Цифри а не букви")

xy_result = [el for el in range(x,y) if el % 3 == 0]
print(xy_result)

N = [random.randint(-10, 10) for i in range(10)]
print(N)
print("Мінімальний додатнє число:", min([el for el in N if el > 0]))

product = 1
for i in [el for el in N if not el == 0]:
  product *= i
print("Добуток віс не нульових елементів:", product)

print([el for el in N if not el == 0][::-1])