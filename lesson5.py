from collections import namedtuple

#1 - masala
# Student = namedtuple("student", ["age", "name", "group"])
# age = int(input("Yosh:  "))
# name = input("Ism:  ")
# group = input("Group:  ")
# student = Student(age, name, group)
# print(student)

#2 - masala
# Book = namedtuple("book",["title", "author", "year"])
# book = Book("Python", "Anvar narzullayev", 2026)
# print(book.author)

#3 - masala
# Point = namedtuple("point",["x", "y"])
# point = Point(9, 12)
# print(point.x)
# print(point.y)

#4 - masala
# Car = namedtuple("car",["brand", "model", "year"])
# car = Car("chevrolet", "coblt ", 2026)
# print(car.brand, car.model, car.year)

#5 - masala
# Student = namedtuple("student", ["name", "age", "score"])
# students = [
#     Student("Ali", 18, 85),
#     Student("Vali", 19, 92),
#     Student("Hasan", 18, 78),
#     Student("Husan", 20, 95),
#     Student("Sardor", 19, 88)
# ]
# max_ball = max( students, key=lambda x: x.score)
# print(max_ball)

#6 - masala
# Product = namedtuple("product",["name", "price", "quantity"])
# products = [
#     Product("Olma", 10000, 5),
#     Product("Banan", 15000, 3),
#     Product("Uzum", 20000, 2),
#     Product("Anor", 25000, 4)
# ]
# natija = sum(
#     i.price * i.quantity
#     for i in products
# )
# print(natija)

#7 - masala
# Epmloyee = namedtuple("epmloyee",["name", "salary"])
# employee = Epmloyee("Ali", 2500000)
# new_employee = employee._replace(
#         salary=employee.salary * 1.2
#     )
# print(new_employee)
# print(employee)

#8 - masala
# City = namedtuple("city",["name", "population"])
# cities = [
#     City("Toshkent", 3200000),
#     City("Samarqand", 600000),
#     City("Andijon", 550000),
#     City("Namangan", 950000),
#     City("Fargona", 450000),
#     City("Buxoro", 300000),
#     City("Nukus", 350000),
#     City("Qarshi", 280000),
#     City("Moskva", 13000000),
#     City("Istanbul", 15000000)
# ]
# print([city.name for city in cities if city.population > 1000000])

#9 - masala
# from collections import defaultdict
# Student = namedtuple("student",["name", "faculty", "gpa"])
# students = [
#     Student("Ali", "IT", 3.5),
#     Student("Vali", "IT", 3.2),
#     Student("Hasan", "Economics", 3.8),
#     Student("Husan", "Economics", 3.6),
#     Student("Bekzod", "Medicine", 3.5)
# ]
# groups = defaultdict(list)
# for i in students:
#     groups[i.faculty].append(i.gpa)
# for x, gpas in groups.items():
#     print(x, "-->", sum(gpas)/len(gpas))

#10 - masala
# Order = namedtuple("order", ["order_id", "customer", "amout"])
# orders = [
#     Order(1, "Ali", 500000),
#     Order(2, "Vali", 1200000),
#     Order(3, "Ali", 800000),
#     Order(4, "Hasan", 2000000),
#     Order(5, "Vali", 300000)
# ]

# max_order = max(orders, key=lambda x: x.amout)
# print(max_order)

# min_order = min(orders, key=lambda x: x.amout)
# print(min_order)

# sum_order  = sum(i.amout for i in orders)/ len(orders)
# print(sum_order)

# count = len([ i for i in orders if i.amout > 1000000])
# print(count)

# dict_ = {}
# for i in orders:
#     if i.customer not in dict_:
#         dict_[i.customer] = 0
#         dict_[i.customer] += i.amout
# print(dict_)

# top = max(dict_, key=dict_.get)
# print(top)


