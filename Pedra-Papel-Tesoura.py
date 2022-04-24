"""
- Adicionar armazenamento de resultados e enviar após o final do jogo, em uma forma comparativa.

N° da partida| Resultado Jogador 1| Resultado Jogador 2| Ganhador| Pontuçao jogador 1| Pontuçao Jogador 2



"""
from random import random 

valor1 = ()
valor2 = ()
player1 = None
player2 = None
pontuacao1 = int(0)
pontuacao2 = int(0)

def jogadores():
    #Esta funçao serve para definir o nome dos players
    print("Escreva o nome do Player 1")    
    global player1
    player1 = input().title()

    print("Escreva o nome do player 2")
    global player2
    player2 = input().title()

    print(f"{player1} VS {player2}\n")

def pedra_papel_tesoura1 ():
    #Esta Funçao define o resultado do Player1 em um valor de 0 a 1
    global valor1
    valor1 = random()
    if  0.66 > valor1 > 0.33 :
        valor1 = "Pedra"        
        print (f"\t Mao do {player1} = {valor1}")
    elif valor1 > 0.66:
        valor1 = "Papel"
        print (f"\t Mao do {player1} = {valor1}")
    elif valor1 < 0.33:
        valor1 = "Tesoura"
        print( f"\t Mao do {player1} = {valor1}")

def pedra_papel_tesoura2 ():
    #Esta Funçao define o resultado do Player1 em um valor de 0 a 1
    global valor2
    valor2 = random()
    if  0.66 > valor2 > 0.33 :
        valor2 = "Pedra"      
        print (f"\t Mao do {player2} = {valor2}")
    elif valor2 > 0.66:
        valor2 = "Papel"
        print (f"\t Mao do {player2} = {valor2}")
    elif valor2 < 0.33:
        valor2 = "Tesoura"
        print( f"\t Mao do {player2} = {valor2}")
    
def resultado_pedra_papel_tesoura ():
    #Esta funçao define quem ganhou a disputa
    global valor1, valor2
    global mao1, mao2
    mao1 = valor1
    mao2 = valor2
    if mao1 == "Papel" and mao2 == "Tesoura":                                 
        print (f"\n \t {player2} ganhou com {mao2}!")
        mao2 = 1      

    elif mao1 == "Papel" and mao2 == "Pedra":                          
        print (f"\n \t {player1} ganhou com {mao1}!")
        mao1 = 1

    elif mao1 == "Pedra" and mao2 == "Papel":                         
        print (f"\n \t {player2} ganhou com {mao2}!")
        mao2 = 1

    elif mao1 == "Pedra" and  mao2 == "Tesoura":                              
        print (f"\n \t {player1} ganhou com {mao1}!")
        mao1 = 1          

    elif mao1 == "Tesoura" and mao2 == "Pedra" :                           
        print (f"\n \t {player2} ganhou com {mao2}!")
        mao2 = 1 

    elif mao1 == "Tesoura" and  mao2 == "Papel":                                
        print (f"\n \t {player1} ganhou com {mao1}!")
        mao1 = 1 
    elif mao1 == mao2:                                                    
        print (f"\t Empate com {mao1}")

def placar():
    #Esta funçao serve para o placar do jogo
    global pontuacao2, pontuacao1, player1, player2
    if mao1 == 1:       
        pontuacao1 = pontuacao1 + 1
        print(f"\n\t{player1} = {pontuacao1}\n\t{player2} = {pontuacao2}")

    if mao2 == 1:
        pontuacao2 = pontuacao2 + 1
        print(f"\n\t{player1} = {pontuacao1}\n\t{player2} = {pontuacao2}")     

def jogar_novamente():
    print('\n\t Deseja jogar novamente, digite "Sim".')
    jogar = bool(input())
    while jogar == True:
        print("\n\n\n\n")
        pedra_papel_tesoura1 ()
        pedra_papel_tesoura2 ()
        resultado_pedra_papel_tesoura ()
        placar()
        print('\n\t Deseja jogar novamente, digite qualquer coisa.')
        jogar = bool(input())
    print("\n \tFoi Divertido, Volte sempre!")

def jogar():
    jogadores()
    pedra_papel_tesoura1 ()
    pedra_papel_tesoura2 ()
    resultado_pedra_papel_tesoura ()
    placar()
    jogar_novamente()  

jogar()


