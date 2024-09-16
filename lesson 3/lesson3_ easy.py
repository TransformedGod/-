#1

# def func(x, y, z):
#     return print(f'{x.capitalize()}, {y} год(а), проживает в городе {z.capitalize()}.')
#
# name = input("Введите имя: ")
# age = input("Введите возраст: ")
# town = input("Введите город: ")
#
# func(name, age, town)


#2

# def func(x, y, z):
#     return max(x, y, z)
#
# x = int(input("Введите число: "))
# y = int(input("Еще одно: "))
# z = int(input("И еще одно: "))
#
# print(func(x, y, z))

# or

x = int(input("Введите число: "))
y = int(input("Еще одно: "))
z = int(input("И еще одно: "))

func = list(lambda x, y, z: max(x, y, z))
print(func)


#3

# def func(*args):
#     return max(*args, key=len)
#
# list_args = []
#
# while True:
#     i = input("Введите что-нибудь, или введите 0 для остановки: ")
#     if i == "0":
#         print("Ок")
#         break
#     else:
#         list_args.append(i)
#
# result = func(list_args)
# print(f"Ваш лучший результат: {result}")
