#1 - masala
# def read_lines(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             yield line.strip()


# for item in read_lines("data.txt"):
#     print(item)       

#2 - masala
# def even_numbers(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             numbers = line.split(" , ")

#             for num in numbers:
#                 num = int(num.strip())

#                 if num % 2 == 0:
#                     yield num

# for n in even_numbers("numbers.txt"):
#     print(n)

#3 - masala
# def long_lines(filename):
#     with open(filename, "r") as file:
#         for line in file:

#             line = line.strip()

#             if len(line) > 5:
#                 yield line

# for item in long_lines("data.txt"):
#     print(item)

#4 - masala
# def square_numbers(filename):
#     with open(filename, "r") as file:
#         for line in file:

#             num = int(line.strip())

#             yield num ** 2

# for n in square_numbers("numbers.txt"):
#     print(n)

#5 - masala
# def fayl_a(filename):
#     with open (filename, "r") as file:
#         for line in file:
#             soz = line.split()


#             for i in line:
#                 yield i

# for x in fayl_a("data.txt"):
#     print(x)

#6 - masala
# users_table = [
#     {"id": 1, "name": "Ali"},
#     {"id": 2, "name": "Vali"},
#     {"id": 3, "name": "Sami"}
# ]

# def soz_user(users_list):
#     for user in users_list:
#         yield user["name"]

# for name in soz_user(users_table):
#     print(name)

#7 - masala
# products_table = [
#     {"id": 1, "name": "olma", "price": 5000},
#     {"id": 2, "name": "banan", "price": 12000},
#     {"id": 3, "name": "nok", "price": 8000}
# ]

# def product(products_list):
#     for product in products_list:
#         if product["price"] > 10000:
#             yield product

# for x in product(products_table):
#     print(x)

#8 - masala
# users_table = [
#     {"id": 1, "name": "Ali", "email": "ali@mail.com"},
#     {"id": 2, "name": "Vali", "email": "vali@mail.com"},
#     {"id": 3, "name": "Sami", "email": "sami@mail.com"}
# ]

# def email(email_list):
#     for i in email_list:
#         yield i["email"]

# for s in email(users_table):
#     print(s)

#9 - masala
# users_table = [
#     {"id": 1, "name": "Ali"},
#     {"id": 2, "name": "Muhammadali"},
#     {"id": 3, "name": "Sami"}
# ]
# def get_name(users_list):
#     for i in users_list:
#         yield i["name"]

# ebg_uzu_ism = ""

# for x in get_name(users_table):
#     if len(x) > len(ebg_uzu_ism):
#         ebg_uzu_ism = x

# print("eng uzun ism: ", ebg_uzu_ism)

#10 - masala
# def pagination_generator(products_list, sahifa_hajmi = 5):
#     boshlanishi = 0
#     while boshlanishi < len(products_list):
#         tugash = boshlanishi + sahifa_hajmi
#         pachka = products_list[boshlanishi:tugash]
#         yield pachka

#         boshlanishi += sahifa_hajmi
# products_table = ["olma", "banan", "nok", "behi", "anor", "uzum", "gilos", "shaftoli", "o'rik", "anjir", "qovun", "tarvuz"]
# sahifa = 1
# for i in pagination_generator(products_table, 5):
#     print(f"{sahifa}-sahifa:", i )
#     sahifa += 1
