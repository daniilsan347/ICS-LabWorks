# Laba No7 -- Task 1
# Завдання  1:  зобразити  2d  графік  функції  відповідно  своєму  варіанту  та 
# зберегти у .png файл.
# Y(x)=(x^3)+cos(15*x), x=[-2...2]

import sys
from numpy import * 
import matplotlib.pyplot as plt 

x = linspace(-2, 2)
y = (x**3)+cos(15*x)

plt.plot(x, y, label="(x^3)+cos(15*x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(sys.path[0]+"/figOutputTask1.png")