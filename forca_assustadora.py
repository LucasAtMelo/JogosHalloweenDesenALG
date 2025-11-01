from random import choice

MAXIMO_ERROS = 6
letras_certas = []
letras_erradas = []
erros = 0 

palavras_halloween = ['ABOBORA', 'MEDO', 'MORCEGO', 'FANTASMA', 'NOITE', 'BRUXA', 'ARREPIO']
palavra_certa = choice(palavras_halloween)

while erros < MAXIMO_ERROS:
    palavra_atual = ''

    for letra in palavra_certa:
        if letra in letras_certas:
            palavra_atual += letra + ' '
        else: 
            palavra_atual += '_'
        
    print(f'Palavra Atual: {palavra_atual}')
    print(f'Erros: {erros}/{MAXIMO_ERROS}')
    print(f'Letras erradas: {letras_erradas}')

    if '_' not in palavra_atual: 
        print('Acertou!!')
        break
    
    tentativa = input('Digite uma letra: ').strip().upper()

    if len(tentativa) != 1 or not tentativa.isalpha(): 
        print('Digite apenas uma letra!')
    
    elif tentativa in letras_certas or tentativa in letras_erradas:
        print(f'A letra {tentativa} já foi tentada!')
    
    elif tentativa in palavra_certa:
        print('Tem essa letra na palavra! ')
        letras_certas.append(tentativa)
    else:
        print(f'A letra {tentativa} não pertence a palavra')
        letras_erradas.append(tentativa)
        erros += 1
