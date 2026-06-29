
# String48
# def string48(text):
#     words = text.split(' ')
#     res_words = []
#     for w in words:
#         if not w:
#             res_words.append('')
#             continue
#         first = w[0]
#         new_w = first + ''.join('.' if c == first else c for c in w[1:])
#         res_words.append(new_w)
#     return ' '.join(res_words)

# String49
# def string49(text):
#     words = text.split(' ')
#     res_words = []
#     for w in words:
#         if not w:
#             res_words.append('')
#             continue
#         last = w[-1]
#         new_w = ''.join('.' if c == last else c for c in w[:-1]) + last
#         res_words.append(new_w)
#     return ' '.join(res_words)
# String50
# def string50(text):
#     words = text.split()
#     words.reverse()
#     return ' '.join(words)

# String51
# def string51(text):
#     words = text.split()
#     words.sort()
#     return ' '.join(words)

# String52
# def string52(text):
#     words = text.split(' ')
#     res_words = []
#     for w in words:
#         if w:
#             res_words.append(w[0].upper() + w[1:])
#         else:
#             res_words.append('')
#     return ' '.join(res_words)

# String53
# def string53(text):
#     punctuations = ".,!?;:-()\"'"
#     count = 0
#     for char in text:
#         if char in punctuations:
#             count += 1
#     return count

# String54
# def string54(text):
#     count = 0
#     for char in text:
#         if char.isupper():
#             count += 1
#     return count

# String55
# def string55(text):
#     words = text.split()
#     if not words:
#         return ""
#     max_w = words[0]
#     for w in words:
#         if len(w) > len(max_w):
#             max_w = w
#     return max_w

# String56
# def string56(text):
#     words = text.split()
#     if not words:
#         return ""
#     min_w = words[0]
#     for w in words:
#         if len(w) <= len(min_w):
#             min_w = w
#     return min_w

# String57
# def string57(text):
#     words = text.split()
#     return ' '.join(words)

# String58
# def string58(path):
#     parts = path.split('\\')
#     file_with_ext = parts[-1]
#     file_name = file_with_ext.split('.')[0]
#     return file_name