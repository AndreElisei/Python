import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um número entre 1 e 10: '))
    if chute > valor_aleatorio:
        print('chute um valor mais baixo')
    elif chute < valor_aleatorio:
        print('chute um valor mais alto')
    else:
        print('voce acertou')
        acertou = True