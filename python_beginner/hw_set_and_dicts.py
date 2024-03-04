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
#     password = input('Введите пароль : ')
#     user=dict.fromkeys([user_name],password)
# print(user)

#8
# peoples={'Aliya' : 'programmer',
#          'Bermet': 'barista',
#          'Luiza' : 'teacher',
#          'Altyn' : 'doctor',
#          'Alina' : 'nurse'
#              }
# for name, profession in peoples.items():
# print(f'Здравствуйте "{name}"\nПрекрасная профессия\n"{profession}"\n')

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