import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time() - start
        print(f"Время выполнения: {time.time() - start}")
        return finish
    return wrapper

@timer
def fun():
    a = ""
    for i in range(100000):
        for j in "qwerty":
            a += j


if __name__ == "__main__":
    c = fun()
    print(c)