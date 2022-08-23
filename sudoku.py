import random

# Tabela do Sudoku #
tabela0 = [0,0,0,  0,0,0,  0,0,0]
tabela1 = [0,0,0,  0,0,0,  0,0,0]
tabela2 = [0,0,0,  0,0,0,  0,0,0]

tabela3 = [0,0,0,  0,0,0,  0,0,0]
tabela4 = [0,0,0,  0,0,0,  0,0,0]
tabela5 = [0,0,0,  0,0,0,  0,0,0]

tabela6 = [0,0,0,  0,0,0,  0,0,0]
tabela7 = [0,0,0,  0,0,0,  0,0,0]
tabela8 = [0,0,0,  0,0,0,  0,0,0]

    # tabela geral #
tabela = [tabela0, tabela1, tabela2, tabela3, tabela4, tabela5, tabela6, tabela7, tabela8]

# colocar um numero em um lugar aleatorio #
numero_inicial = random.randrange(0,9)
posicao_inicial = random.choice(tabela)
posicao_inicial[random.randrange(0,9)] =  numero_inicial


# Gerar a tabela inicial
# Checar uma tabela aleatoria
# Colocar um numero aleatorio na tabela (antes verificar se ele já existe)
# Se ele não existir, ter uma chance de colocar ele, (entre 1 e 10)

dificuldades = ['facil', 'medio', 'dificil']
dificuldade = 'facil'

def gerar_chance():
    match dificuldade:
        case 'facil':
            return random.randrange(0, 3)
        case 'medio':
            return random.randrange(0, 7)
        case 'dificil':
            return random.randrange(0, 10)

# Gerar tabela checando por duplicados na horizontal
for tabela_atual in tabela:
    # Colocar em uma posicao aleatoria da tabela atual utilizando chances
    for elemento_atual in tabela_atual:
        chance = gerar_chance()
        if chance == 0:
            numero_aleatorio = random.randrange(1, 10)

            # checar se o numero gerado já está na tabela atual
            if numero_aleatorio in tabela_atual:
                pass 
            else:
                tabela_atual[random.randrange(0, 8)] = numero_aleatorio

numeros_vertical_1 = ''

# Checar tabelas verticais
for tabela_atual in tabela:
    elemento = str(tabela_atual[0])
    if elemento in numeros_vertical_1 and elemento != '0':
        print(f'{elemento} já está nos numeros verticais [{numeros_vertical_1[int(elemento)]}]')
        
    else:
        numeros_vertical_1 += elemento

[print(tabela_atual) for tabela_atual in tabela]
contador = 0

