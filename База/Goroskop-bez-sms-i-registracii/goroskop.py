#goroskop.py


print("Вас вітає гороскоп без СМС та регістрації! Заповніть поля")
name = input("Ім'я: ")
surname = input("Прізвище: ")
patronimic = input("По-батькові: ")
sex = input("Ви чоловік чи жінка? [М/Ж] ")

monthOfBirth = input("Якого місяця народження? [Назва] ").lower()
dayOfBirth = int(input("День народження: "))

if (dayOfBirth >= 21 and monthOfBirth == 'березень') and (dayOfBirth <= 20 and monthOfBirth == 'квітень'):
  print("Ви,", surname, name, patronimic, ", є Овеном!")
elif (dayOfBirth >= 21 and monthOfBirth == 'квітень') and (dayOfBirth <= 20 and monthOfBirth == 'травень'):
  print("Ви,", surname, name, patronimic, ", є Телецем!")
elif (dayOfBirth >= 21 and monthOfBirth == 'травень') and (dayOfBirth <= 20 and monthOfBirth == 'червень'):
  print("Ви,", surname, name, patronimic, ", є Близнятами!")
elif (dayOfBirth >= 21 and monthOfBirth == 'червень') and (dayOfBirth <= 20 and monthOfBirth == 'липень'):
  print("Ви,", surname, name, patronimic, ", є Раком!")
elif (dayOfBirth >= 21 and monthOfBirth == 'липень') and (dayOfBirth <= 20 and monthOfBirth == 'серпень'):
  print("Ви,", surname, name, patronimic, ", є Левом!")
elif (dayOfBirth >= 21 and monthOfBirth == 'серпень') and (dayOfBirth <= 20 and monthOfBirth == 'вересень'):
  print("Ви,", surname, name, patronimic, ", є Дівою!")
elif (dayOfBirth >= 21 and monthOfBirth == 'вересень') and (dayOfBirth <= 20 and monthOfBirth == 'жовтень'):
  print("Ви,", surname, name, patronimic, ", є Терезами!")
elif (dayOfBirth >= 21 and monthOfBirth == 'жовтень') and (dayOfBirth <= 20 and monthOfBirth == 'листопад'):
  print("Ви,", surname, name, patronimic, ", є Скорпіоном!")
elif (dayOfBirth >= 21 and monthOfBirth == 'листопад') and (dayOfBirth <= 20 and monthOfBirth == 'грудень'):
  print("Ви,", surname, name, patronimic, ", є Стрілцем!")
elif (dayOfBirth >= 21 and monthOfBirth == 'грудень') and (dayOfBirth <= 20 and monthOfBirth == 'січень'):
  print("Ви,", surname, name, patronimic, ", є Козерогом!")
elif (dayOfBirth >= 21 and monthOfBirth == 'січень') and (dayOfBirth <= 20 and monthOfBirth == 'лютий'):
  print("Ви,", surname, name, patronimic, ", є Водолієм!")
elif (dayOfBirth >= 21 and monthOfBirth == 'лютий') and (dayOfBirth <= 20 and monthOfBirth == 'березень'):
  print("Ви,", surname, name, patronimic, ", є Рибою!")
