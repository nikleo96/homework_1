import timeit

h = "import math"

p1 = """
start = 1
finish = 10000
a = 16
b = 23
c = a*b

my_list = [i for i in range(start, finish+1)]

st_a = math.ceil(start / a) * a
st_b = math.ceil(start / b) * b
st_c = math.ceil(start / c) * c

if st_a < finish+1:
    for i in range(st_a, finish+1, a):
        my_list[i-start] = "fizz"

if st_b < finish+1:
    for i in range(st_b, finish+1, b):
        my_list[i-start] = "buzz"

if st_c < finish+1:
    for i in range(st_c, finish+1, c):
        my_list[i-start] = "fizz buzz"
"""

p2 = """
my_list = []
st = 1
fn = 10000
a = 3
b = 5
c = a * b
for i in range(st, fn+1):
    if i%c == 0:
        my_list.append('FizzBuzz')
    elif i%a == 0:
        my_list.append('Fizz')
    elif i%b == 0:
        my_list.append('Buzz')
    else:
        my_list.append(i)
"""

t2 = timeit.Timer(stmt=p2)
t1 = timeit.Timer(stmt=p1, setup=h)

print(t1.timeit(number=1000))
print(t2.timeit(number=1000))

# print(my_list)



