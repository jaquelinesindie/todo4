#!/usr/bin/python
# teste.py

name_list = []
curriculum_list = []

candidatos = int(input("Digite o número de candidatos no processo seletivo: "))

for x in range(candidatos):
    name = input("Digite o nome do candidato: ")
    curriculum = input("Vaga que o candidato está candidatando {0}".format(name))
    name_list.append(input("Digite o nome do candidato: "))
    curriculum_list.append(curriculum)

d = dict(zip(name_list, curriculum_list))
print(d)