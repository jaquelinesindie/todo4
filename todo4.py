""" ToDo 4 Contratado
    Analisar os currículos cadastrados para uma vaga em uma empresa, ven do se o candidato tem o perfil necessário e quantos estão concorrendo a vaga
"""

""" Funções
"""

def quantidadeCandidatos(num):
    participantes = num.count('candidato(a)') #count funciona em strings
    return f'A quantidade de candidatos a serem cadastrados é {participantes}'

def separaCandidatos(arquivo):
    lista_nova = []
    sub_list = [] 

    for i in arquivo:
        if i.startswith('candidato(a):'):
            if sub_list != []:
                lista_nova.append(sub_list)
                sub_list=[]
        sub_list.append(i)
    lista_nova.append(sub_list)

    return (lista_nova)


# def entrada(candidatos, curriculo):
#     palavraChaveAD = ['python','power', 'sql', 'comunicação']
#     palavraChaveCD = ['python','banco','sql','machine','resolução','estatística', 'r']
#     analistaDados = 0 # variável para contagem do número de analistas
#     cientistaDados = 0 # variável para contagem do número de cientistas
#     count = 0

#     return 

""" Variáveis globais
"""

participantes = 0
txt_string = ''
arquivo = []

""" Processo de extração dos dados
"""

with open('processoSeletivo.txt', encoding='utf-8') as ps:
    linhas = ps.readlines()
    # print(lines)
""" Processo de transformação dos dados
"""

for valor in linhas: # Laço de concatenação da string e extração de caracteres 
    txt_string = txt_string + valor.replace('\n','') + ' '
    txt_string = txt_string.replace(',','')
    txt_string = txt_string.replace(':','')


# print('Tirando os caracteres desnecessários do texto e concatenando em string ',txt_string) # Testes de funcionamento do código

txt_string = txt_string.split() # separa todas as palavras

# print('Split', txt_string) # Testes de funcionamento do código

txt_string = str(txt_string).lower()
txt_string = txt_string.replace('[','') # Retirando os colchetes devido aos processos de tranformações
txt_string = txt_string.replace(']','') # Retirando os colchetes devido aos processos de tranformações

# print('Verificação do tipo',type(txt_string))
# print('Transformando em minúsculo',txt_string)

arquivo = [txt_string] # Transforma o texto em lista

# print('Verificação do tipo',type(arquivo)) # Testes de funcionamento do código
# print('Texto no tipo lista',arquivo) # Testes de funcionamento do código

print(separaCandidatos(arquivo))

participantes = quantidadeCandidatos(txt_string)

print(participantes)

# print(entrada(participantes, arquivo))


