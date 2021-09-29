import math
import fractions

a = 3
b = -14
c = -5

D = b**2 - 4*a*c

if D < 0:
    print("Нет решения")
elif D == 0:
    x = -b / (2*a)
    print("Один корень у уравнения. Ответ:" + str(x))
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Уравнение имеет два решения: x1 = ", str(x1), ", x2 = ", str(x2))
