# from functools import reduce
# sonlar = [1, 2, 3, 4]
# ismlar = ["ali", "vali", "hasan"]
#1 - masala
# natija = list(map(lambda x: x * 2, sonlar))
# print(natija)

#2 - masala
# natija = list(map(lambda x: x ** 2, sonlar))
# print(natija)

#3 - masala
# natija = list(map(lambda x: x + 10, sonlar))
# print(natija)

#4 - masala
# natija = list(map(str, sonlar))
# print(natija)

#5 - masala
# natija = list(map(lambda x: x.upper(), ismlar))
# print(natija)

#6 - masala
# natija = list(filter(lambda x: x % 2 == 0, sonlar))
# print(natija)

# #7 - masala
# natija = list(filter(lambda x: x > 0, sonlar))
# print(natija)

# #8 - masala
# natija = list(filter(lambda x: x > 50, sonlar))
# print(natija)

# #9 - masala
# sozlar = ["python", "olma", "dasturchi"]
# natija = list(filter(lambda x: len(x) > 5, sozlar))
# print(natija)

# #10 - masala
# natija = list(filter(lambda x: x % 3 == 0, sonlar))
# print(natija)

# #11 - masala
# natija = list(map(lambda x: x ** 3, sonlar))
# print(natija)

# #12 - masala
# natija = list(map(lambda x: x % 10, sonlar))
# print(natija)

# #13 - masala
# natija = list(map(len, ismlar))
# print(natija)

# #14 - masala
# natija = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", sonlar))
# print(natija)

# #15 - masala
# gap = "salom dunyo python"
# natija = list(map(lambda x: x.capitalize(), gap.split()))
# print(natija)

# #16 - masala
# def tub(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# natija = list(filter(tub, sonlar))
# print(natija)

# #17 - masala
# natija = list(filter(lambda x: sum(map(int, str(x))) > 10, sonlar))
# print(natija)

# #18 - masala
# natija = list(filter(lambda x: x == x[::-1], sozlar))
# print(natija)

# #19 - masala
# natija = list(filter(lambda x: str(x) == str(x)[::-1], sonlar))
# print(natija)

# #20 - masala
# natija = list(filter(lambda x: x[0].lower() in "aeiou", ismlar))
# print(natija)

# #21 - masala
# natija = reduce(lambda x, y: x + y, sonlar)
# print(natija)

# #22 - masala
# natija = reduce(lambda x, y: x * y, sonlar)
# print(natija)

# #23 - masala
# natija = reduce(lambda x, y: x + " " + y, sozlar)
# print(natija)

# #24 - masala
# natija = reduce(lambda x, y: x if x > y else y, sonlar)
# print(natija)

# #25 - masala
# ismlar = ["Ali", "Vali", "Hasan"]
# ballar = [90, 85, 78]
# natija = list(zip(ismlar, ballar))
# print(natija)

# #26 - masala
# oylar = ["Yanvar", "Fevral", "Mart"]
# raqamlar = [1, 2, 3]
# natija = list(zip(oylar, raqamlar))
# print(natija)

# #27 - masala
# ismlar = ["Ali", "Vali"]
# yoshlar = [20, 21]
# guruhlar = ["N45", "N46"]
# natija = list(zip(ismlar, yoshlar, guruhlar))
# print(natija)

# #28 - masala
# mahsulotlar = ["Olma", "Banan", "Uzum"]
# narxlar = [12000, 18000, 25000]
# natija = list(zip(mahsulotlar, narxlar))
# print(natija)
