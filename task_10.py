a = ['1', '11', '12', '22', '2', '13', '30', '33']

# b = sorted([i for i in a if int(i)%2 == 0], key=lambda x: int(x))
b = [i for i in a if int(i)%2 == 0]

print(b)