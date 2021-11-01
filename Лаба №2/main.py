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
    print("Сортованний список")
    funcs.pprint_list(funcs.quick_sort(N))
    input("[Enter] Продовжити")
  elif user_input == "2":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    while True:
      try:
        print("Елемент для пошуку. Ціле число")
        element = int(input("$: "))
        break
      except ValueError as err:
        print("Неможливо конвертувати у ціле число")
        print(err)
        continue
    funcs.find_el(N, element)
    input("[Enter] Продовжити")
  elif user_input == "3":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    while True:
      try:
        print("Елементи для пошуку. Цілі числа. Розділяти за допомогою\", \"")
        elements_input = input("$: ").split(", ")
        elements = [int(item) for item in elements_input]
        break
      except ValueError as err:
        print("Неможливо конвертувати у ціле число")
        print(err)
        continue
    funcs.find_few_els(N, elements)
    input("[Enter] Продовжити")
  elif user_input == "4":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    print("5 мінімальних чисел")
    funcs.pprint_list(funcs.find_5_min_nums(N))
    input("[Enter] Продовжити")
  elif user_input == "5":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    print("5 максимальних чисел")
    funcs.pprint_list(funcs.find_5_max_nums(N))
    input("[Enter] Продовжити")
  elif user_input == "6":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    print("5 максимальних чисел")
    funcs.pprint_list(funcs.average(N))
    input("[Enter] Продовжити")
  elif user_input == "7":
    N = funcs.gen_randint_list(-10, 10, 25)
    print("Оригінальний список")
    funcs.pprint_list(N)
    print("Список без дублікатів")
    funcs.pprint_list(funcs.remove_duplicates(N))
    input("[Enter] Продовжити")
  elif user_input == "0":
    break
  else:
    print("Невідома команда")