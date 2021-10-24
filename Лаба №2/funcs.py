# Laba No2

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
  result = []
  for el in elements_list:
    found_index = find_el(list, el)
    if found_index != False:
      result.append(tuple([found_index, el]))
  return result.sort(key = lambda item: item[0])