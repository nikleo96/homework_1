import math
import fractions
import decimal

print(decimal.Decimal("-14.0"))
a = input("Введите коэффициент 'a': ")
while True:
    try:
        a = float(a)
        break
    except:
        print("Введите число!!!")
        a = input("Введите коэффициент 'a': ")


b = input("Введите коэффициент 'b': ")
while True:
    try:
        b = float(b)
        break
    except:
        print("Введите число!!!")
        b = input("Введите коэффициент 'b': ")

c = input("Введите коэффициент 'c': ")
while True:
    try:
        c = float(c)
        break
    except:
        print("Введите число!!!")
        c = input("Введите коэффициент 'c': ")

# a = 3
# b = -14
# c = -5


D = b**2 - 4*a*c

if D < 0:
    print("Нет решения")
elif D == 0:
    x = -b / (2*a)
    print("Один корень у уравнения. Ответ:" + str(x))
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Уравнение имеет два решения: x1 = ", str(x1), ", x2 = ", str(round(x2, 2)))


# print("Нет решения") if D < 0 else 

