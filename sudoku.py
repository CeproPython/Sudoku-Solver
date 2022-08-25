import random


def main():
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

    # Gerar a tabela inicial
    # Checar uma tabela aleatoria
    # Colocar um numero aleatorio na tabela (antes verificar se ele já existe)
    # Se ele não existir, ter uma chance de colocar ele, (entre 1 e 10)

    # dificuldades = ['facil', 'medio', 'dificil']
    dificuldade = 'facil'

    def gerar_chance():
        if dificuldade == 'facil':
            return random.randrange(0, 3)
        if dificuldade == 'medio':
            return random.randrange(0, 7)
        if dificuldade == 'dificil':
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
                    tabela_atual[random.randrange(0, 9)] = numero_aleatorio

    numeros_vertical_1 = ''

    # Deprecapted #
    #   Checar tabelas verticais
    #   for tabela_atual in tabela:
    #       elemento = str(tabela_atual[0])
    #       if elemento in numeros_vertical_1 and elemento != '0':
    #           print(f'{elemento} já está nos numeros verticais [{numeros_vertical_1[int(elemento)]}]')
    #       else:
    #           numeros_vertical_1 += elemento

    [print(tabela_atual) for tabela_atual in tabela]

    primeiros = []

    def checar_primeiros(n):
        primeiros_string = ''
        for i in tabela:
            primeiros_string += str(i[n])
        else:
            primeiros.append(primeiros_string)

    for casa_a_casa in range(9):
        checar_primeiros(casa_a_casa)

    def tem_duplicados(palavra):
        tem = False
        temp = []
        for i in palavra:
            if i in temp and i != '0':
                i = '0'
                continue
            else:
                temp.append(i)
        else:
            if tem:
                main()
            return tem

    contador = 0
    for i in primeiros:
        contador += 1
        if tem_duplicados(i):
            print(f'Tabela {contador} tem duplicados!')

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

    apareceram = ''
    for i in celulas:
        for j in i:
            for k in j:
                if k != 0:
                    apareceram += str(k)

        print(apareceram)
        apareceram = ''


main()
# while True:
#    main()

