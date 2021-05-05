import random
def cria_baralho():
    cartas =['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    random.shuffle(cartas)
    return cartas

def extrai_naipe(carta):
    if len(carta)>2:
        naipe = carta[2]
    else:
        naipe = carta[1]
    return naipe

def extrai_valor(carta):
    if len(carta)>2:
        valor = carta[0]+carta[1]
    else:
        valor = carta[0]
    return valor

def lista_movimentos_possiveis(baralho,i):
    lista_possiveis =[]
    if i ==0:
        return lista_possiveis
    if len(baralho) <4:
        if extrai_naipe(baralho[i])== extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]):
            lista_possiveis.append(1)
    elif len(baralho)>3:
        if extrai_naipe(baralho[i])== extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]):
            lista_possiveis.append(1) 
        if (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-3])) and (i-3) >=0:
            lista_possiveis.append(3)
    return lista_possiveis

def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    possibilidades = False
    for i in range(len(baralho)):
        if len(lista_movimentos_possiveis(baralho,i)) != 0:
            possibilidades = True
    return possibilidades   

print('Paiciencia acordeao')
print('o estado atual do baralho é:')
baralho = cria_baralho()

while possui_movimentos_possiveis(baralho) != False:    
    for i in range(len(baralho)):
        print('{0}. {1}'.format(i+1, baralho[i]))
    entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
    possibilidades = lista_movimentos_possiveis(baralho, int(entrada)-1)
    if len(possibilidades) == 0:
        print("A carta {} não pode ser movida".format(baralho[int(entrada)-1]))
        entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
    elif len(possibilidades) == 2:
        print("Escolha sobra qual carta você que empilhar o {}".format(baralho[int(entrada)-1]))
        print('{0}. {1}'.format(1, baralho[int(entrada)-2]))
        print('{0}. {1}'.format(2, baralho[int(entrada)-4]))
        escolha2 = ''
        while escolha2 != '1' and escolha2 != '2':
            escolha2 = input('Digite o número de sua escolha (1 ou 2): ')
            if escolha2 == '1':
                baralho = empilha(baralho, int(entrada)-1, int(entrada)-2)
            elif escolha2 == '2':
                baralho = empilha(baralho, int(entrada)-1, int(entrada)-4)
            else:
                print('Escolha inválida')
    elif len(possibilidades) == 1:
        baralho = empilha(baralho, int(entrada)-1, int(entrada)-2)

    possui_movimentos_possiveis(baralho) == False
    
