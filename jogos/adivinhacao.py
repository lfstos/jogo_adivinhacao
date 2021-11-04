import random

print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randint(1, 100)
total_de_tentativas = 0

print('Qual o nível de dificuldade?')
print(('{}\n{}\n{}'.format('1 - Fácil', '2 - Médio', '3 - Difícil')))
nivel_dificuldade = int(input('Defina o nível: '))

if (nivel_dificuldade == 1):
    total_de_tentativas = 20
elif (nivel_dificuldade == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute_str = input('Digite o seu número: ')
    print(f'Você digitou {chute_str}')
    chute = int(chute_str)
    
    if (chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 entre 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Você acertou')
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior do que o número secreto')
        elif(menor):
            print('Você errou! O seu chute foi menor do que o número secreto')
print('O número secreto é {}'.format(numero_secreto))

print('Fim do jogo')