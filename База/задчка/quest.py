while True:
  print("room1")
  room1 = input("У які двері уввійти? ")
  if room1 == "1":
    door1 = True
  elif room1 == "2":
    door2 = True
  else:
    print("Я твоя, не панимать")
    continue
  while True:
    if door1:
      print("bear Room")
      room2 = input("Шо робити? ")
      if room2 == "1":
        print("Твоя побеждать")
      elif room2 == "2":
        print("Твоя умирац")
      elif room2 == "3": 
        print("Твоя умирац")
      else:
        print("Я твоя, не панимать")
        continue
    elif door2:
      print("Ktulhu room")
      room3 = input("Шо робити? ")
      if room3 == "1": 
        print("Твоя умирац")
      elif room3 == "2": 
        print("Твоя побеждать")
      elif room3 == "3": 
        print("Твоя умирац")
      else:
        print("Я твоя, не панимать")
        continue
    break
  restart = input("Конец пути. Заново? [Y/N]").lower()
  if restart == "y":
    act = True
    continue
  elif restart == "n":
    break
  else:
    print("Читать и печатать научись")
