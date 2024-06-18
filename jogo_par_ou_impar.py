import random
print("Vamos jogar?")
print("O nome do jogo é par ou impar, você começa!")
opcoes = ["par", "impar"]
escolhaJogador = input("Escolha: par ou impar?  ")

while (escolhaJogador != opcoes[0]) and (escolhaJogador != opcoes[1]):
    escolhaJogador = input("Opção invalida! Escolha: par ou impar?  ")

jogadorNumero = input("Escolha um numero inteiro    ")

while (type(jogadorNumero) is not int):
    try:
        jogadorNumero = int(jogadorNumero)
    except:
        try:
            jogadorNumero = int(input("Escolha um numero inteiro    "))
        except:
            continue


npcNumero = random.randint(1,10)

print("NPC escolheu " + str(npcNumero))

if((jogadorNumero+npcNumero) % 2 == 0):
    if(escolhaJogador == opcoes[0]):
        print("Jogador Ganhou")
    else:
        print("Jogador Perdeu")
else:
    if(escolhaJogador == opcoes[1]):
        print("Jogador Ganhou")
    else:
        print("Jogador Perdeu")