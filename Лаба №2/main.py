# Laba No2 -- Main script

import funcs
import random

while True:
  print("======[ Демонстрація функцій ]=======")
  print("Завантаженно функції з модулю funcs")
  print("1. Швидке сортування")
  print("2. Пошук елементу за значенням")
  print("3. Пошук послідовності елементів")
  print("4. Пошук перших п’яти мінімальних елементів")
  print("5. Пошук перших п’яти максимальних елементів")
  print("6. Пошук середнього арифметичного")
  print("7. Видалення дублікатів")
  print("0. Вийти")

  user_input = input("$: ")

  if user_input == "1":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    print("Оброблений список")
    funcs.pprint_list(funcs.quick_sort(N))
  elif user_input == "2":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    while True:
      try:
        print("Елемент для пошуку. Ціле число")
        element = int(input("$: "))
        break
      except ValueError:
        print("Неможливо конвертувати у ціле число")
        continue
    funcs.find_el(N, element)
  elif user_input == "3":
    pass
  elif user_input == "4":
    pass
  elif user_input == "5":
    pass
  elif user_input == "6":
    pass
  elif user_input == "7":
    pass
  elif user_input == "0":
    break
  else:
    print("Невідома команда")