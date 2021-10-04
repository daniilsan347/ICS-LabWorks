#mama-ya-mathematik
import math

print("Функція z(x)\n")

x = float(input("x = "))
z = 2*math.sin(x) + math.sqrt(x)

print("\nЗначення z у точці x:", z,"\n----------------------------")

print("Найбільша цифра у натуральному числі\n")

N = input("Введіть натуральне число: ")

try:
  buffer = 0
  for i in N:
    if int(i)%9 == 0:
      buffer = 9
    elif int(i)%9 > buffer:
      buffer = int(i)
  print(f"Найбільша цифра: {buffer}, індекс {N.index(str(buffer))}\n----------------------------")
except ValueError:
  print("Наступний раз вводи число")

print("Список натуралів та операції над ним\n")

naturalList = [-9,-14,-7,-6,-1,0,4,16,15,13,8]
print("Мінімальне число:", min(naturalList))
oddList = []
for i in naturalList:
  if not(i%2 == 0):
    oddList.append(i)
oddMean = sum(oddList)/len(oddList)
print("Середнє арифметичне непарних елементів:", oddMean)
negativeList = []
for i in naturalList:
  if i < 0:
    negativeList.append(i)
negativeList.sort()
print("Від'ємні числа:", negativeList)