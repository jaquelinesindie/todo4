# # dict1 = {'color': 'blue', 'shape': 'circle'}
# # dict2 = {'colore': 'red', 'number': 42}
 
# # dict1.update(dict2)
# # print(dict1)

# #A simple dictionary
# d = {'a': True, 42:0.3, 0.2:'Hi'}
# print(d)
# e = dict(a=0, b=1, c=2, d=3)
# print(e)
# #Acessing a value
# print(d['a'])
# #Adding a new key-value pair
# d['3'] = 23
# print(d)
# #Looping through all key-value pairs
# fav_numbers = {'eric':18, 'everton':20}
# for name, number in fav_numbers.items():
#     print(name + ' loves a number ' + str(number))
# #Looping through all keys
# for name in fav_numbers.keys():
#     print(name + ' is a better person')
# #Looping through all the values
# for number in fav_numbers.values():
#     print(f'{number} is a pretty number')
# #Looping through all the keys in reverse order
# for name in sorted(fav_numbers.keys(), reverse=True):
#  print(f"{name}: of person")

# #Getting the value associated with get()
# fav_name = fav_numbers.get('eric')
# fav_number = fav_numbers.get(18,0)

# print(fav_name)
# print(fav_number)

# # Start with an empty list.
# users = []
# # Make a new user, and add them to the list.
# new_user = {
#  'last': 'fermi',
#  'first': 'enrico',
#  'username': 'efermi',
#  }
# users.append(new_user)
# # Make another new user, and add them as well.
# new_user = {
#  'last': 'curie',
#  'first': 'marie',
#  'username': 'mcurie',
#  }
# users.append(new_user)
# # Show all information about each user.
# for user_dict in users:
#     for k, v in user_dict.items():
#         print(f"{k}: {v}")
#         print("\n") 

# squares = {x: x**2 for x in range(5)}

# print(squares)

# name_list = []
# curriculum_list = []

# for x in range(curriculo):
#     name = input("Digite o nome do candidato(a): ")
#     curriculum = input("Digite o objetivo do candidato(a) {0}: ".format(name))
#     resume = input('Digite o resumo do currículo do candidato: ')
#     name_list.append(name)
#     curriculum_list.append(curriculum)
#     curriculum_list.append(resume)

# d = dict(zip(name_list, curriculum_list))