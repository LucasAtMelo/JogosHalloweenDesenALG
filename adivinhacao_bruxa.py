from random import randint

numero = randint(1, 50)
MAXIMO_TENTATIVAS = 7
numero_tentativas = 0
acerto = False

while numero_tentativas < MAXIMO_TENTATIVAS:
    try:
        palpite = int(input('Digite seu palpite: '))
    except ValueError:
        print('Digite uma entrada válida!')

    if palpite == numero:
        print('ACERTOU!!!') 
        acerto = True 
        break

    elif palpite < numero: 
        print('MUITO BAIXO! O número é maior que seu palpite!')
        numero_tentativas += 1

    elif palpite > numero:
        print('MUITO ALTO! O número é menor que seu palpite!')
        numero_tentativas += 1

if acerto:
    print(f'Você ganhou com {numero_tentativas} tentativas')

else:
    print(f'Você não conseguiu acertar, o número era {numero}')
    
