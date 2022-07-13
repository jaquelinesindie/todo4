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

#!/usr/bin/python
# teste.py

# name_list = []
# curriculum_list = []

# candidatos = int(input("Digite o número de candidatos no processo seletivo: "))

# for x in range(candidatos):
#     name = input("Digite o nome do candidato: ")
#     curriculum = input(
#         "Vaga que o candidato está candidatando {0}".format(name))
#     name_list.append(input("Digite o nome do candidato: "))
#     curriculum_list.append(curriculum)

# d = dict(zip(name_list, curriculum_list))
# print(d)

# my_list = ['France, the weather is nice', 'the house is beautiful', 'we have a fresh start here', 'France, the dinner is amazing',
#            'the lady is lovely', 'France, the house is beautiful', 'the location is fascinating']

# new_list = []
# sub_list = []
# for i in my_list:
#     if i.startswith('candidato(a),'):
#         if sub_list != []:
#             new_list.append(sub_list)
#             sub_list=[]

#     sub_list.append(i)
# new_list.append(sub_list)

# print(new_list)

# my_list = ['France, the weather is nice', 'the house is beautiful', 'we have a fresh start here', 'France, the dinner is amazing', 'the lady is lovely', 'France, the house is beautiful','the location is fascinating']


# def separaCandidatos(index=len(my_list) - 1):
#     if index < 0:
#         return []
#     if not my_list[index].startswith('France,'):
#         data = split_list(index - 1)
#         data[-1].append(my_list[index])
#         return data
#     else:
#         return split_list(index - 1) + [[my_list[index]]]


# print(split_list())

# arquivo = ['France, the weather is nice', 'the house is beautiful', 'we have a fresh start here', 'France, the dinner is amazing',
#            'the lady is lovely', 'France, the house is beautiful', 'the location is fascinating']

# lista_nova = []
# sub_list = [] 

# for i in arquivo:
#     if i.startswith('France,'):
#         if sub_list != []:
#             lista_nova.append(sub_list)
#             sub_list=[]

#     sub_list.append(i)
# lista_nova.append(sub_list)

# print(lista_nova)


# dicionario = dict(zip(range(0,len(lista_nova)), lista_nova))
# print(dicionario)

# sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
# sentence_list = sentence.split()
# sentence_dictionary = {}

# for item in sentence_list:
#     if item not in sentence_dictionary:
#         sentence_dictionary[item] = 0
#     sentence_dictionary[item] += 1
# word_counts = sentence_dictionary
# print(word_counts)
txt_string = ''
txt = ''
with open('processoSeletivo.txt', encoding='utf-8') as ps:
    linhas = ps.readlines()
    # print(lines)
""" Processo de transformação dos dados
"""

for valor in linhas: # Laço de concatenação da string e extração de caracteres 
    txt_string = txt_string + valor.replace('\n','') + ' '
    txt_string = txt_string.replace(',','')
    txt_string = txt_string.replace(':','')

# print('Tirando os do texto e concatenando em string ', txt_string)
txt_string = txt_string.split() # separa todas as palavras
# print('Split', txt_string)
txt_string = str(txt_string).lower()
txt_string = txt_string.replace('[','') # Retirando os colchetes devido aos processos de tranformações
txt_string = txt_string.replace(']','') # Retirando os colchetes devido aos processos de tranformações
# print(txt_string)
# print('Transformando em minúsculo',txt_string)
arquivo = [txt_string] # Transforma o texto em lista
# print(type(arquivo))
# print(arquivo)

lista_nova = []
sub_list = [] 

for i in arquivo:
    if i.startswith("'candidato(a)'"):
        if sub_list != []:
            lista_nova.append(sub_list)
            sub_list=[]
    sub_list.append(i)
lista_nova.append(sub_list)

print('Lista nova \n',lista_nova)


# dicionario = dict(zip(range(0,len(lista_nova)), lista_nova))
# print(dicionario)