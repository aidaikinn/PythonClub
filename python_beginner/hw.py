# a=2**3
# b=3**2

# if a > b:
#     print(f"Значение первой переменной ({a}) больше ({b})")

# elif a<b:
#     print(f"Значение первой переменной ({a}) меньше ({b})")

# else: 
#     print("Значение данных двух переменных равны")

"""генераторы"""

#1 
# n = int(input("Введите число:"))
# summa=0
# for i in range(1, n+1):
#  summa +=i
# print(sum)

#2 
# n=int(input("Введите число:"))
# x = 0
# for i in range (2, n//2+1):
#     if (n % i ==0):
#         x=x+1
#     if (x<=0):
#         print(f"Число {n} является простым")
#         break
#     else :
#         print(f"Число {n} не является простым")
#         break

#3
# nums = input("Введите числа:").split()
# print(nums)
# nums_list=list(map(int,nums)) //в данном случае альтернативный вариант добавления в список
# nums_list =[int(num) for num in nums]
# arif = sum(nums_list)/len(nums_list)
# print(arif)

#4 
# nums_list = []
# nums = input("Введите числа:").split()
# nums_list=list(map(int,nums))
# print(nums_list)
# maximum = max(num for num in nums_list)
# minimum = min(num for num in nums_list)
# print(f"Максимальное значение из списка чисел: {maximum}")
# print(f"Минимальное значение из списка чисел: {minimum} ")

#5
# lines = input("Введите:")
# empty_line = iter (line for line in lines) 
# if lines:
#     print("Строка не пуста!")
# else:
#     print("Строка пуста!")

#6?

#7
list = ['red', 'yellow', 'grey', 'black', 'white']
maximum=max(len(elem)for elem in list) #((elem for elem in list), key = len)
minimum=min((elem for elem in list), key = len)
print(f"Наибольший элемент из списка: {maximum}")
print(f"Наименьший элемент из списка: {minimum} ")

#8
# list = ['красный', 'белый', 'черный', 'белый', 'желтый', 'красный', 'серый', 'белый']
# corr_list = []
# for color in list:
#     if color not in corr_list:
#         corr_list.append(color)
# print(corr_list)

#9 
# nums = (3,5,4,7,8,2)
# summa=sum(num for num in nums)
# print(f"Сумма элементов: {summa}")

#10 
# fruits = ('watermelon', 'apple', 'kiwi', 'banana')
# maximum = max((elem for elem in fruits), key = len)
# print(f"Наибольший элемент в данном кортеже: {maximum}")

#11

#12
# dictionary = {"apple": 5, "banana": 2, "orange": 3}
# user_key=input("Введите ключ, который вам необходим:")
# if user_key in dictionary.keys():
#     print("Данный ключ есть в наличии")
# else:
#     print("Данный ключ отсутствует")
    
#13
# nums = int(input("Введите число:"))
# if nums % 2 ==0: 
#     print(f"Число {nums} является четным")
# else:
#     print(f"Число {nums} является нечетным")

#12
# year = int(input("Введите год:"))
# if year %400 ==0:
#     print (f"{year} год является високосным годом")
# else:
#     print(f"{year} год не является високосным")