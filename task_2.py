input_str = input("Введите уравнение вида 'y=ax+b': ")

param_x = input("Введите х: ")
param_x = float(param_x)

right_str = input_str[input_str.find("=")+1:]
position_x = right_str.find("x")

param_a = float(right_str[:position_x])
param_b = float(right_str[position_x+1:])

result = param_a * param_x + param_b
print(result)

# решение через split() быстрее
 