# Laba No2 - Functions module

import random
from typing import *

quick_sort = lambda list: sorted(list)

def find_el(list: List, element: Any):
  """
  Returns item index if item is found, otherwise returns False
  """
  try:
    el_index = list.index(element)
    print(f"Element \"{list[el_index]}\" at index [{el_index}]")
    return el_index
  except ValueError:
    print(f"There is no element \"{element}\"")
    return False

def find_few_els(list: List, elements_list: List):
  """
  Returns list of tuples with index and item. If there is no searched item, it won't apear in list.
  """
  result = []
  for el in elements_list:
    found_index = find_el(list, el)
    if found_index != False:
      result.append(tuple([found_index, el]))
  return result.sort(key = lambda item: item[0])

def find_5_min_nums(list: List):
  """
  Returns list of 5 minimum numbers. If there is string in list, returns False
  """
  list_float = []
  result = []
  try:
    for el in list:
      list_float.append(float(el))
  except ValueError as err:
    print("List contains strings.", err)
    return False
  for el in range(5):
    min_num = min(list_float)
    result.append(min_num)
    list_float.remove(min_num)
  return result

def find_5_max_nums(list: List):
  """
  Returns list of 5 maximum numbers. If there is string in list, returns False
  """
  list_float = []
  result = []
  try:
    for el in list:
      list_float.append(float(el))
  except ValueError as err:
    print("List contains strings.", err)
    return False
  for el in range(5):
    min_num = max(list_float)
    result.append(min_num)
    list_float.remove(min_num)
  return result

def average(list: List):
  """
  Returns average float number of all numbers in list
  """
  list_float = []
  try:
    for el in list:
      list_float.append(float(el))
  except ValueError as err:
    print("List contains strings.", err)
  result = sum(list_float)/len(list_float)
  return result

def remove_duplicates(list: List):
  """
  Returns list without duplicates
  """
  sorted_list = quick_sort(list)
  for i in range(len(sorted_list)-1):
    if sorted_list[i] == sorted_list[i+1]:
      sorted_list.pop(i)
  return sorted_list

def pprint_list(list: List):
  print("[ ", end="")
  for i in range(len(list)-1):
    print(list[i], end=", ")
  print(list[-1], "]")

def gen_randint_list(min, max, count):
  """Generates list of random integers"""
  return [random.randint(min, max) for i in range(count)]

def gen_randfloat_list(count):
  """Generates list of random floats"""
  return [random.random()*100 for i in range(count)]
