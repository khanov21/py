# # 1 masala
# yigindi = lambda a, b: a + b
# print(yigindi(5, 3))

# # 2 masala
# kvadrat = lambda x: x ** 2
# print(kvadrat(4))

# # 3 masala
# juft_toq = lambda x: "Juft" if x % 2 == 0 else "Toq"
# print(juft_toq(7))

# # 4 masala
# uzunlik = lambda s: len(s)
# print(uzunlik("Python"))

# # 5 masala
# salom = lambda ism: f"Salom, {ism}"
# print(salom("Ali"))

# # 6 masala
# sonlar = [7, 2, 9, 1]
# print(sorted(sonlar, key=lambda x: x))

# # 7 masala
# talabalar = [("Ali", 90), ("Vali", 75), ("Hasan", 85)]
# print(sorted(talabalar, key=lambda x: x[1]))

# # 8 masala
# sozlar = ["olma", "dasturchi", "kitob"]
# print(sorted(sozlar, key=lambda x: len(x)))

# # 9 masala
# nuqtalar = [(2, 5), (1, 3), (4, 1)]
# print(sorted(nuqtalar, key=lambda x: x[1]))

# # 10 masala
# mahsulotlar = [("Olma", 15000), ("Banan", 25000), ("Uzum", 18000)]
# print(sorted(mahsulotlar, key=lambda x: x[1]))

# # 11 masala
# talabalar = [("Ali", 85), ("Vali", 92), ("Hasan", 78)]
# print(sorted(talabalar, key=lambda x: x[1], reverse=True))

# # 12 masala
# sonlar = [34, 27, 19, 42]
# print(sorted(sonlar, key=lambda x: x % 10))

# # 13 masala
# fayllar = [("a.txt", 200), ("b.pdf", 500), ("c.doc", 300)]
# print(sorted(fayllar, key=lambda x: x[1], reverse=True))

# # 14 masala
# talabalar = [("Ali", 20, 85), ("Vali", 19, 90), ("Hasan", 20, 80)]
# print(sorted(talabalar, key=lambda x: (x[1], x[2])))

# # 15 masala
# odamlar = [("Ali", "Karimov"), ("Vali", "Toshmatov"), ("Hasan", "Saidov")]
# print(sorted(odamlar, key=lambda x: x[1][-1]))

# # BONUS 16
# sonlar = [1, 2, 3]
# print(list(map(lambda x: x ** 3, sonlar)))

# # BONUS 17
# ismlar = ["Ali", "Muhammad", "Vali"]
# print(sorted(ismlar, key=lambda x: len(x), reverse=True))

# # BONUS 18
# mahsulotlar = ["Olma", "Banan", "Anor"]
# print(sorted(mahsulotlar, key=lambda x: x[0]))

# # BONUS 19
# gap = "Men python backend organyapman"
# print(sorted(gap.split(), key=lambda x: len(x)))

# # BONUS 20
# sonlar = [5, 9, 2, 11, 3]
# eng_katta = lambda x: max(x)
# eng_kichik = lambda x: min(x)
# print(eng_katta(sonlar))
# print(eng_kichik(sonlar))
