################################################1
#bik = input("Введите строку чтобы повернуть приложение")
#revers_user_str = bik[:: -1]
#print(revers_user_str)

############################2
# a = input("ВВедите строку чтобы посчитать кол-во букв и кол-во цифр:")
# b = 0 # для дижит
# c = 0 # для альфа
# for i in a:
#     if i.isdigit():
#         b += 1
#     elif i.isalpha():
#         c += 1
#
# print(f"кол-во цифр в предложение: {b}")
# print(f"кол-во букв в предложение: {c}")

#############################################3

# a = input("ВВедите строку чтобы посчитать  сколько раз в строке встречается искомый символ:")
# b = input("ВВедите искомый символ")
# print(a.count(b))

###############################4
# a = input("ВВедите строку чтобы посчитать  сколько раз в строке встречается искомый символ:")
# b = input("ВВедите искомое слово")
# print(a.count(b))

####################5
a = input("ВВедите строку:")
b = input("ВВедите слово, которое нужно заменить:")
c = input("ВВедите слово для замены:")
print(a.replace(b, c))