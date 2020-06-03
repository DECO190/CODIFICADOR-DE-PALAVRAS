def cab(b):
    print('=' * 40)
    print('\033[1m{}\033[m'.format(b).center(45))
    print('=' * 40)
alf= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
while True:
    cab('MENU')
    print('1> CODIFICAR MENSAGEM')
    print('2> DESCODIFICAR MENSAGEM ')
    print("3> SAIR")
    print('='*40)
    opi = int(input('OPÇÃO: '))
    if opi not in [1,2,3]:
        while True:
            print('OPÇÃO INVÁLIDA!')
            opi = int(input('OPÇÃO: '))
            if opi in [1,2,3]:
                break
    if opi == 1:
        cab('CODIFICAÇÃO')
        while True:
            try:
                pal= str(input('> DIGITE UMA PALAVRA: ')).lower().strip()
                for let in pal:
                    lug = alf.index(let)
            except ValueError:
                print('DIGITE UMA PALAVRA SEM ESPAÇOS!')
            else:
                print(('PALAVRA CODIFICADA: '),end='')
                for let in pal:
                    lug = alf.index(let)
                    print((alf[lug + 3]), end='')
                print(" ")
                break
    if opi == 2:
        cab('DESCODIFICAÇÃO')
        while True:
            try:
                dec = str(input('> DIGITE A PALAVRA CODIFICADA: '))
                for le in dec:
                    pos = alf.index(le)
            except ValueError:
                print('DIGITE UMA PALAVRA SEM ESPAÇOS!')
            else:
                print(('PALAVRA DESCODIFICADA: '), end='')
                for le in dec:
                    pos = alf.index(le)
                    print((alf[pos - 3]), end='')
                print(" ")
                break
    if opi == 3:
        break