#37 - masala
# def index_generator(s1, s2):
#     start = 0
#     while True:
#          i = s1.find(s2, start)
#          if i == -1:
#               break
#          yield i
#          start = i + 1

# import time
# def deco(func):
#      def wrapper(*args, **kwargs):
#           start_time = time.time()
#           result = func(*args, **kwargs)
#           end_time= time.time()
#           print(f"[Dekarator] Bajarish vaqti: {end_time - start_time:.6f} soniya")
#           print(f"[ Dekarator] Almashtirishlar soni: 1 ta")
#           return result
#      return wrapper

# @deco
# def replase(s1, s2, s3):
#      indexs = list(index_generator(s1, s2))
#      if not indexs:
#           return s1
#      last_ind = indexs[-1]
#      new_s1 = s1[:last_ind] + s3 + s1[last_ind +len(s2):]
#      return new_s1

# S1 = "olma anor olma behi olma"
# S2 = "olma"
# S3 = "nok"

# natija = replase(S1, S2, S3)
# print("Natija:", natija)

#38 - masala
import time
# def decarator_x(func):
#     def wrapper(*args, **kwargs):
#         res_str, count = func(*args, **kwargs)
#         print(f"[Decarator] natijaviy satr uzunligi: {len(res_str)}")
#         print(f"[Decarator] almashtiriligan elementlar soni: {count}")
#         return res_str
#     return wrapper

# def generator_index(s1, s2):
#     x = len(s2)
#     i = 0
#     while i <= len(s1) - x:
#         if s1[i:i + x ] == s2:
#             yield i
#             i += x
#         else:
#             i += 1

# @decarator_x
# def replase_x(s1, s2, s3):
#     index = list(generator_index(s1, s2))
#     count = len(index)
#     x = s1.replace(s2, s3)
#     return x, count

# s1 = "olma anor olma nok olma"
# s2 = "olma"
# s3 = "behi"
# print("natija: ", replase_x(s1, s2, s3))

#39 - masala
# def decarator_x(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f"[Decarator] Ajratib olingan belglar soni: {len(result)}")
#         print(f"[Decarator] Bajarilish vaqti{( end_time - start_time:.6f)} sekund")
#         return result
#     return wrapper

#def index_generator(text):
#     for x, i in enumerate(text):
#         if i == '':
#             yield i

# @decarator_x
# def get_betwen(text):
#     spaces = list(index_generator(text))
#     if len(spaces) < 2:
#         return ""
#     return text[spaces[0] + 1 : spaces[1]]
# print("natija: ", get_betwen(" Pythonda django beckend developer"))

#40 - masala
# def string40_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"[Decorator] Natijaviy qism uzunligi: {len(result)}")
#         return result
#     return wrapper

# @string40_decorator
# def get_between_first_last_space(text):
#     spaces = list(index_generator(text))
#     if len(spaces) < 2:
#         return ""
#     return text[spaces[0] + 1 : spaces[-1]]

# print("Natija:", get_between_first_last_space("Men bugun juda ko'p kod yozdim"))

#41 - masala
# def string41_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         count = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"[Decorator] Topilgan so'zlar soni: {count}")
#         print(f"[Decorator] Bajarilish vaqti: {(end - start):.6f} sekund")
#         return count
#     return wrapper


# def word_generator(text):
#     words = text.split()
#     for word in words:
#         yield word

# @string41_decorator
# def count_all_words(text):
#     words_list = list(word_generator(text))
#     return len(words_list)

# print("Natija:", count_all_words("Najot Ta'lim zamonaviy kasblar akademiyasi"))

# import time

# def word_generator(text):
#     for word in text.split():
#         yield word


# String42
# def string42_decorator(func):
#     def wrapper(*args, **kwargs):
#         count = func(*args, **kwargs)
#         print(count)
#         return count
#     return wrapper

# @string42_decorator
# def count_same_edge_letters(text):
#     count = 0
#     for word in word_generator(text.upper()):
#         if len(word) > 0 and word[0] == word[-1]:
#             count += 1
#     return count


# String43
# def string43_decorator(func):
#     def wrapper(*args, **kwargs):
#         match_count, total_count = func(*args, **kwargs)
#         print(match_count)
#         print(total_count)
#         return match_count
#     return wrapper

# @string43_decorator
# def count_words_with_A(text):
#     total_count = 0
#     match_count = 0
#     for word in word_generator(text.upper()):
#         total_count += 1
#         if "A" in word:
#             match_count += 1
#     return match_count, total_count


# String44
# def string44_decorator(func):
#     def wrapper(*args, **kwargs):
#         count = func(*args, **kwargs)
#         print(count)
#         return count
#     return wrapper

# @string44_decorator
# def count_words_with_exactly_three_A(text):
#     count = 0
#     for word in word_generator(text.upper()):
#         if word.count("A") == 3:
#             count += 1
#     return count


# String45
# def string45_decorator(func):
#     def wrapper(*args, **kwargs):
#         min_len = func(*args, **kwargs)
#         print(min_len)
#         return min_len
#     return wrapper

# @string45_decorator
# def find_min_word_length(text):
#     words = list(word_generator(text))
#     if not words:
#         return 0
#     return min(len(word) for word in words)

# String46
# def string46_decorator(func):
#     def wrapper(*args, **kwargs):
#         max_len = func(*args, **kwargs)
#         print(max_len)
#         return max_len
#     return wrapper

# @string46_decorator
# def find_max_word_length(text):
#     words = list(word_generator(text))
#     if not words:
#         return 0
#     return max(len(word) for word in words)


# String47
# def string47_decorator(func):
#     def wrapper(*args, **kwargs):
#         res_str, word_count = func(*args, **kwargs)
#         print(len(res_str))
#         print(word_count)
#         return res_str
#     return wrapper

# @string47_decorator
# def join_words_with_dot(text):
#     words = list(word_generator(text))
#     res_str = ".".join(words)
#     return res_str, len(words)