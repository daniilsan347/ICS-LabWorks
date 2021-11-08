while True:
  try:
    el1 = float(input("Перше число: "))
  except ValueError:
    print("Літери не числа, давай знову")
    continue
  while True:
    oper = input("Оператор [+, -, /, *]: ")
    if oper in "*/-+":
      break
    else:
      print("Не правильний оператор")
  try:
    el2 = float(input("Друге число: "))
  except ValueError:
    print("Літери не числа, давай знову")
    continue
  if oper == "+":
    print(el1 + el2)
  elif oper == "-":
    print(el1 - el2)
  elif oper == "*":
    print(el1 * el2)
  elif oper == "/":
    if el2 == 0:
      print("Ділення на нуль")
    else:
      print(el1 / el2)
  else:
    print("error")