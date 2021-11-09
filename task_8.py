def counter(i):
    def action():
        nonlocal i
        i += 1
        return i
    return action

i = 0
while i < 9:
    i = counter(i)()
    print(i)