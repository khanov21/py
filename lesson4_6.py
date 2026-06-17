import time

# 1-masala
def decorator(func):
    def wrapper():
        print("START")
        func()
        print("END")
    return wrapper

@decorator
def salom():
    print("Salom")

salom()


# 2-masala
def show_args(func):
    def wrapper(*args):
        print(args)
        return func(*args)
    return wrapper

@show_args
def add(a, b):
    return a + b

print(add(5, 3))


# 3-masala
def get_double(func):
    def wrapper():
        return func() * 2
    return wrapper

@get_double
def son():
    return 10

print(son())


# 4-masala
def musbat(func):
    def wrapper(lst):
        yangi = []
        for i in lst:
            if i > 0:
                yangi.append(i)
        return func(yangi)
    return wrapper

@musbat
def chiqar(lst):
    return lst

print(chiqar([-2, 5, -1, 7]))


# 5-masala
def counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(count)
        func()
    return wrapper

@counter
def hello():
    print("Hello")

hello()
hello()
hello()


# 6-masala
def only_even(func):
    def wrapper(lst):
        natija = []
        for i in lst:
            if i % 2 == 0:
                natija.append(i)
        return func(natija)
    return wrapper

@only_even
def sonlar(lst):
    return lst

print(sonlar([1, 2, 3, 4, 5, 6]))


# 7-masala
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@timer
def test():
    time.sleep(2)

test()


# 8-masala
def sort_result(func):
    def wrapper():
        return sorted(func())
    return wrapper

@sort_result
def sonlar2():
    return [5, 2, 8, 1]

print(sonlar2())


# 9-masala
def positive(func):
    def wrapper(lst):
        return func([x for x in lst if x > 0])
    return wrapper

def greater_10(func):
    def wrapper(lst):
        return func([x for x in lst if x > 10])
    return wrapper

@positive
@greater_10
def test2(lst):
    return lst

print(test2([-5, 3, 12, 20]))


# 10-masala
def filter_all(func):
    def wrapper(lst):
        natija = []
        for i in lst:
            if i > 10 and i % 2 == 0:
                natija.append(i)
        return func(natija)
    return wrapper

@filter_all
def chiqar2(lst):
    return lst

print(chiqar2([2, 4, 12, 14, 15, 20]))


# 11-masala
def slow_warning(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        if end - start > 1:
            print("Sekin ishladi")
    return wrapper

@slow_warning
def test3():
    time.sleep(2)

test3()


# 12-masala
def to_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@to_upper
def ism():
    return "mirzaali"

print(ism())


# 13-masala
def square(func):
    def wrapper(lst):
        yangi = []
        for i in lst:
            if i > 0 and i % 2 == 0:
                yangi.append(i ** 2)
        return func(yangi)
    return wrapper

@square
def test4(lst):
    return lst

print(test4([-5, 2, 4, -1, 6]))


# 14-masala
def logger(func):
    def wrapper(a, b):
        start = time.time()
        result = func(a, b)
        end = time.time()

        print("Natija:", result)
        print("Vaqt:", end - start)

        return result
    return wrapper

@logger
def kopaytir(a, b):
    return a * b

kopaytir(5, 4)


# 15-masala
def only_int(func):
    def wrapper(a, b):
        if type(a) == int and type(b) == int:
            return func(a, b)

        print("Faqat int kiriting")
    return wrapper

@only_int
def add2(a, b):
    return a + b

print(add2(5, 10))


# 16-masala
def no_negative(func):
    def wrapper(a, b):
        result = func(a, b)

        if result < 0:
            print("Manfiy son")
        else:
            return result
    return wrapper

@no_negative
def ayir(a, b):
    return a - b

print(ayir(10, 5))
print(ayir(5, 10))


# 17-masala
def save_file(func):
    def wrapper(x):
        result = func(x)

        file = open("result.txt", "a")
        file.write(str(result) + "\n")
        file.close()

        return result
    return wrapper

@save_file
def kvadrat(x):
    return x * x

print(kvadrat(5))
print(kvadrat(8))