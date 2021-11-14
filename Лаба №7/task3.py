# Laba No7 -- Task 3
# Text: Катерина
# Завдання 3:  Зобразити гістограму частоти появи у певному тексті звичайних, 
# питальних та окличних речень, а також речень,  що завершуються трикрапкою 
# та зберегти у .png файл.

import pylab
import sys

with open(sys.path[0]+'/kateryna.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    sentencesCount = {
        ".": data.count(". "),
        "!": data.count("! "),
        "?": data.count("? "),
        "...": data.count("... "),
    }

xdata = list(sentencesCount.keys())
ydata = [sentencesCount[i] for i in xdata]
pylab.bar(xdata, ydata) 
pylab.title("Катерина, кількіть речень")
pylab.savefig(sys.path[0]+"/figOutputTask3.png")
