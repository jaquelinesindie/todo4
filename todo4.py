""" ToDo 4 Contratado
    Analisar os currículos cadastrados para uma vaga em uma empresa, ven do se o candidato tem o perfil necessário e quantos estão concorrendo a vaga
"""

""" Funções
"""
def entrada(candidatos, curriculo):
    palavraChaveAD = ['python','power bi', 'sql', 'comunicação']
    palavraChaveCD = ['python','banco','dados','machine','learning','resolução','problemas','estatística', 'r']
    analistaDados = 0 # variável para contagem do número de analistas
    cientistaDados = 0 # variável para contagem do número de cientistas
    count = 0

    # while candidatos:
        
    #     for i in curriculo:
    #         if i in 

    return 




""" Variáveis globais
"""
participantes = 0
txt_string = ''
arquivo = []

""" Processo de extração dos dados
"""

with open('processoSeletivo.txt', encoding='utf-8') as ps:
    lines = ps.readlines()
    print(lines)
""" Processo de transformação dos dados
"""

for valor in lines: # Laço de concatenação da string
    txt_string = txt_string + valor.replace('\n','') + ' '

print('Tirando os \n do texto e concatenando em string ',txt_string)
txt_string = txt_string.split() # separa todas as palavras
# print('Split', txt_string)
txt_string = str(txt_string).lower()
print(type(txt_string))
print('Transformando em minúsculo',txt_string)
arquivo = [txt_string] # Transforma o texto em lista
print(type(arquivo))
print(arquivo)

participantes = txt_string.count('candidato(a)') #count funciona em strings
print(f'A quantidade de candidatos a serem cadastrados é {participantes}')

print(entrada(participantes, arquivo))

