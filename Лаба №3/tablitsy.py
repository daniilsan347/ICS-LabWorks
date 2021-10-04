# tablitsy

import csv

# Розрахунок середньої ціни за 4 місяці
def countAvg(arr):
  for i in range(1, 4) : avgPrice =+ float(arr[i])
  return round(avgPrice/4, 2)

# Створення списку з даними про ринкові ціни
prices = []
with open("table1.csv", "r") as table1: 
  pricesTable = csv.reader(table1)
  for row in pricesTable:
    try:
      # Додавання до списку словника з номером товару, середньою ціною та роком запису про ціни 
      prices.append(dict({'id':row[0], 'avg':countAvg(row), 'year':row[5]})) 
    except ValueError:
      continue

# Створення списку з даними про базові ціни
goods = {}
with open("table2.csv", "r") as table2:
  goodsTable = csv.reader(table2)
  for row in goodsTable:
    try:
      # Перевірка на потрібні рядки
      int(row[0])
      # Додання до словника номерного словника з назвою та базовою ціною товару
      goods[row[0]] = {}
      goods[row[0]]['name'] = row[1]
      goods[row[0]]['price'] = float(row[3])
    except ValueError:
      continue

# Заголовок результативної таблиці
resultTable = [['Найменування товару', 'Рік', 'Середня ціна, крб', 'Розднібна ціна, крб', 'Рівень змін']]

index = 1
for row in prices:
  resultTable.append([])
  resultTable[index].append(goods[row['id']]['name'])
  resultTable[index].append(row['year']) 
  resultTable[index].append(row['avg']) 
  resultTable[index].append(goods[row['id']]['price']) 
  resultTable[index].append(round(row['avg']/goods[row['id']]['price'], 2)) 
  index += 1
print(resultTable)