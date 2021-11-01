# Laba No4 -- Variant 11

import sys

rawSentences = []

with open(sys.path[0] + "/duna.txt", "r", encoding="utf-8") as book: 
  lines = book.readlines()
  for line in lines:
    if line != "\n" and line != "~ ~ ~\n":
      # rawSentences.append(line.split(" "))
      sentencesInLine = line.split(".")
      for i in sentencesInLine:
        if i != "":
          rawSentences.append(i)

# Госпаде, что там есть такого на 400+ слов в одном предложении
counter = {}
sentCount = 0

for line in rawSentences:
  wordsCount = len(line)
  if wordsCount in counter:
    counter[wordsCount] += 1
  else:
    counter[wordsCount] = 1
  sentCount += 1

print(counter)
print(sentCount)

print(len(counter) / sentCount)