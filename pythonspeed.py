# # # # # 

# # # # #handle exceptions

# # # # try:
# # # #     x = 7 / 0
# # # # except Exception as e:
# # # #     print(e)
# # # # finally:
# # # #   print('finally')

# # # #lambda

# # # x = lambda x, y: x + y
 
# # # print(x(2, 32))

# # #map and filter
# # x = [1,2,4,5,7,8,7,8,12,54,623]

# # mp = map(lambda i: i + 2, x)
# # print(list(mp))

# # def func(i):
# #     i = i 
# #     return i % 2 == 0

# # mp = filter(lambda i: i % 2 == 0, x)
# # print(list(mp))

# #F strings
# tim = 89
# x = f'hello { 6 + 8} {tim} { 67 + 9}'
# print(f'hello { tim}')