import time
#1 - Masala
def decrator(func):
    def wrapper():
        print("---START---")
        func()
        print("---END---")
    return wrapper

#2 - masala
# def show_args(func):
#     def wrapper(*args):
#         print("Args: ", args)
#         return func(*args)
#     return wrapper

#3 - masala
# def get_double(func):
#     def wrapper():
#         return func() * 2
#     return wrapper


#4 - masala

# def musbat_s(func):
#     def wrapper(list):
#         return func([x for x in lst if > 0])
#     return wrapper

#5 masala
# def counter(func):
#     count = 0
#     def wrapper(*args):
#         nonlocal count
#         count += 1

#         print(f"funksiya {count} marta chiqarildi")
#         return func(*args)
#     return wrapper

#6 - masala
# def only_even(func):
#     def wrapper(lst):
#         return func([x for x in lst if x % 2 == 0])
#     return wrapper


# 7 - masala
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{end - start:.3f} sekund")
#         return result
#     return wrapper

#8 - Masala
# def sort_result(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args, **kwargs))
#     return wrapper


#9 - masala
# def positive(func):
#     def wrapper(lst):
#         return func([x for x in lst if x > 0])
#     return wrapper


# def greater_than_10(func):
#     def wrapper(lst):
#         return func([x for x in lst if x > 10])
#     return wrapper

#10 - masala
# def filter_all(func):
#     def wrapper(lst):
#         lst = [x for x in lst if x > 0]
#         lst = [x for x in lst if x % 2 == 0]
#         lst = [x for x in lst if x > 10]
#         return func(lst)
#     return wrapper


#11 - masala
# def slow_warning(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()

#         if end - start > 1:
#             print("Sekin ishlayotgan funksiya!")

#         return result
#     return wrapper


# #12 - masala
# def to_upper(func):
#     def wrapper(*args):
#         return func(*args).upper()
#     return wrapper


#13 - masala
# def positive2(func):
#     def wrapper(lst):
#         return func([x for x in lst if x > 0])
#     return wrapper


# def even2(func):
#     def wrapper(lst):
#         return func([x for x in lst if x % 2 == 0])
#     return wrapper


# def square(func):
#     def wrapper(lst):
#         return func([x ** 2 for x in lst])
#     return wrapper

#14 - masala
# def logger(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()

#         print("\nFunksiya:", func.__name__)
#         print("Args:", args)
#         print("Natija:", result)
#         print(f"Vaqt: {end - start:.4f} sekund")

#         return result
#     return wrapper


# #15 - masala
# def only_int(func):
#     def wrapper(*args):
#         if not all(isinstance(x, int) for x in args):
#             print("Xato: faqat integer kerak")
#             return
#         return func(*args)
#     return wrapper


# #16 - masala
# def no_negative_result(func):
#     def wrapper(*args):
#         result = func(*args)
#         if result < 0:
#             print("Xatolik: natija manfiy!")
#             return
#         return result
#     return wrapper


# #17 - masala
# def save_to_file(func):
#     def wrapper(*args):
#         result = func(*args)
#         with open("result.txt", "a") as f:
#             f.write(str(result) + "\n")
#         return result
#     return wrapper