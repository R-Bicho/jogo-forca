import re

print('Bem vindo ao jogo da forca\n\nIMPORTANTE:')
print('\t- Você possui 6 chances para acertar a palavra;\n\
    \t- Repetir uma letra por engano não computará erro;\n\
    \t- Existe distinção de palavras com acento e sem acento;\n\
    \t- Palavras compostas são aceitas.\n')

palavra = input('Digite uma palavra para brincar: ').lower()
palavra_reg_exp = re.compile(r'^[a-z A-Z á-ú Á-Ú]+\-?[a-z A-Z á-ú Á-Ú]*$')
letra_reg_exp = re.compile(r'^[a-z A-Z á-ú Á-Ú -]+$')

if not palavra_reg_exp.match(palavra):
    raise TypeError('A palavra deve conter apenas letras')

tentativas = []
chances = 6
erros = 0

while True:
    letra = input('Digite uma letra: ').lower().strip()

    if not letra_reg_exp.match(letra):
        print('Digite apenas letras')
        continue

    if letra in tentativas:
        print('Você ja tentou essa letra, escolha outra!')
        continue

    if len(letra) > 1:
        print('Precisa digitar apenas uma letra')
        continue
    else:
        tentativas.append(letra)

    nova_palavra = ''
    for letra_secreta in palavra:
        if letra_secreta in tentativas:
            nova_palavra += letra_secreta
        else:
            nova_palavra += '*'

    if letra in nova_palavra:
        print(nova_palavra)
    else:
        erros += 1
        print(f'{nova_palavra}, você possui mais {chances - erros} chances')

    if erros == 6:
        print('Você perdeu!')
        break

    if nova_palavra == palavra:
        print('Parabéns você venceu!')
        break
