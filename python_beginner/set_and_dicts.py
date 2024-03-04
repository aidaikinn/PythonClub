#class_js={'Aktan', 'Aigul', 'Mayrash', 'Artyom'}
#class_python = {'Malik', 'Aigul', 'Eldos', 'Aktan'}

#inter = class_js.intersection(class_python)
#print(inter)
#print(class_js&class_python)

#diff = class_js.difference(class_python)
#diff2=class_python.difference(class_js)
#print = (class_js & class_python)
#print(diff)
#print(diff2)

#print(class_js.union(class_python))
#print(class_js | class_python)

#fruits = {'apple','banana','kiwi','tangerin'}
#vegetables={'carrot','potato','tomato','apple'}
#fruits.intersection_update(vegetables)
#print(fruits)
#print(vegetables)

#fruits.difference_update(vegetables)
#print(fruits)

#my_set={(1,2,3), '123123'}
#my_set.remove('123123')
#my_set.discard('123123')

#my_set.pop()
#print(my_set)

"""Словари {dict}"""

#passport={'name': 'Meerim', 'last_name': 'Kayratova', 'age': 25, 'gender': 'F'}

#print(passport['name'])
#passport ['age']

#print(dict(name='Islam', age = 222))
#print(dict9[ (name,'Islam', age = 222)

#new_dict=dict.fromkeys(['a','b'],10)
#print(new_dict)

#new_dict={
#    'name': 'Ak-Maral',
 #   [1,2,3,4]: 'ERRORRROR'}

#car= {
   # 'dict1': {'name': 'Islamchik', 'age': 190},
#'marka':'Toyota',
#'model': 'Camry',
#"color": "black",
#"volume": 3.2,
#"year": 2012,
#'kuzov': 'Купе'}

#print(car['marka'])
# print(car['kuzov'])

# print(car.get('kuzov', 'ТАКОГО КЛЮЧА НЕТ'))

#print(car.setdefault('kuzov', 'Седан'))

""""Домашка"""
#1 удаляет число 7
#set_1={1,3,5,7,9,0}
#set_1.remove(7)
#print(set_1)

#2 находит схожие объекты
#set_1={'Aliya','Alina', 'Milessa'}
#set_2={'Alina','Akmaral', 'Nurkyz'}
#inter = set_1.intersection_update(set_2)
#print(inter)
#print(set_1&set_2)

#3 находит объекты, которых нет в set2
#set_2={'Aliya','Alina', 'Milessa'}
#set_3={'Alina','Akmaral', 'Nurkyz'}
#set_3.difference_update(set_2)

#print(set_3)

#4 удаляет необходимый элемент по индексу 
#set_1=['cat', 'rabbit','dog', 'puppy', 'fox']
#set_1.pop(3)
#print(set_1)

#5 
#menu={'manty': 120, 'lagman': 120, 'borsh': 150}
#menu['bash_barmak']=130#добавление нового блюда 
#print(menu)

#menu['lagman']=135#обновление цены блюда лагман
#print(menu)

#menu.pop('borsh')#удаляет объект из меню 
#print(menu)

#menu={'manty': 120, 'lagman': 120, 'borsh': 150}
#drinks=dict.fromkeys(['Coca-Cola', 'Sprite', 'Fanta'],60)#добавление напитков с помощью ключа
#print(drinks)

#6


#7
# d=dict()
# for _ in range(3):#цикл запрашивает имя и пароль по заданному числу
#     user_name=input('Введите ваше имя : ')
#     password = input('Введите парроль : ')
#     user=dict.fromkeys([user_name],password)
# print(user)

#8
# peoples={'Aliya' : 'programmist',
#              'Bermet': 'barista',
#              'Luiza' : 'teacher',
#              'Altyn' : 'doctor',
#              'Alina' : 'nurse'
#              }
# for name, profession in peoples.items():
   
#     print(f'Здравствуйте "{name}"\nПрекрасная профессия\n"{profession}"\n')

#9 
# ch=set()
# for _ in range (10): 
#     chislo = int(input("Введите число: "))
#     ch.add(chislo)
#     ch_tuple=tuple(ch)

# print(ch)

#10
# countries={'Аргентина', 'Суринам', 'Боливия', 'Бразилия', 'Венесуэла', 'Гайана', 'Колумбия', 'Парагвай', 'Перу', 'Суринам', 'Уругвай', 'Чили', 'Эквадор'}
# con=[]
# [con.append(x) for x in countries if x not in con]#генератор списков
# print(str(con))

#11
# suitcase = []
# suitcase.append("swimsuit")
# suitcase.append("hoodie")
# suitcase.append("jeans")
# suitcase.append("cap")
# suitcase.append("sunglasses")
# suitcase.remove('sunglasses')
# print(suitcase)