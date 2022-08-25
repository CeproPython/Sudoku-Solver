import random


tem2 = False
tabela_sudoku = []


def gerar():
    global tem2

    # Tabela do Sudoku #
    tabela0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    tabela3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    tabela6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tabela8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # tabela geral #
    tabela = [tabela0, tabela1, tabela2, tabela3, tabela4, tabela5, tabela6, tabela7, tabela8]

    # colocar um numero em um lugar aleatorio #
    numero_inicial = random.randrange(0, 9)
    posicao_inicial = random.choice(tabela)
    posicao_inicial[random.randrange(0, 9)] = numero_inicial

    dificuldade = 'medio'

    # Função de gerar chance, gera um número em uma escala dependendo da dificuldade
    def gerar_chance():
        if dificuldade == 'facil':
            return random.randrange(0, 2)
        
        if dificuldade == 'medio':
            return random.randrange(0, 5)
        
        if dificuldade == 'dificil':
            return random.randrange(0, 10)

    # Adicionar os números aleatoriamente pela tabela (de 1 a 9)
    for tabela_atual in tabela:
        for elemento_atual in tabela_atual:
            
            chance = gerar_chance()
            
            if chance == 0:
                numero_aleatorio = random.randrange(1, 10)

                # Ignorar se ele já está, se não, colocar ele
                if numero_aleatorio in tabela_atual:
                    pass
                
                else:
                    tabela_atual[random.randrange(0, 9)] = numero_aleatorio

    # Todas as células (3x3)
    celulas = [
        [tabela[0][0:3], tabela[1][0:3], tabela[2][0:3]],
        [tabela[0][3:6], tabela[1][3:6], tabela[2][3:6]],
        [tabela[0][6:9], tabela[1][6:9], tabela[2][6:9]],

        [tabela[3][0:3], tabela[4][0:3], tabela[5][0:3]],
        [tabela[3][3:6], tabela[4][3:6], tabela[5][3:6]],
        [tabela[3][6:9], tabela[4][6:9], tabela[5][6:9]],

        [tabela[6][0:3], tabela[7][0:3], tabela[8][0:3]],
        [tabela[6][3:6], tabela[7][3:6], tabela[8][3:6]],
        [tabela[6][6:9], tabela[7][6:9], tabela[8][6:9]],
    ]

    lst = []
    apareceram = ''

    # Sistema para checar todas as casas em todos os blocos
    # Se o número que está sendo checado na casa já existe nela, chama a função denovo
    # Assim previnindo numeros duplicados em uma casa
    for bloco in celulas:
        for casa in bloco:
            for numero in casa:
                if numero != 0:
                    apareceram += str(numero)
                    lst.append(numero)

        for e in lst:
            # list.count() retorna a quantidade de vezes que um elemento aparece em uma lista
            
            if lst.count(e) > 1:
                tem2 = True
                break

        if tem2:
            break
            
        lst.clear()
        apareceram = ''

    for i in tabela:
        global tabela_sudoku
        
        tabela_sudoku.append(i)


gerar()

for i in tabela_sudoku:
    print(i)
