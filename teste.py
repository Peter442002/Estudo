"""import PyPDF2 as py2

pdf = open("pdfteste.pdf", "rb")

pdf_reader = py2.pdfFileReader(pdf)

n = pd_reader.numPages

for i in range(0, n):
    print("Página {}".format(i + 1))
    page = pdf_reader.getPage(i)
    print(page.extractText())

"""


def menu():    
    print('eae vei, bora jogar?\n \t Digite:\n"1" para Sim, "2" para não\n')
    bora = int(input('1. Sim, vou ganhar facil! \n''2. nem, quero naum \n')) 
    if bora == 1:
        print("Vai se fuder, entao!\n essa porra ainda nao esta pronta!")
        #game()
    print('bele, até a proxima')
    
menu()


"""def game():
    jogada=0
    jogador1 =1
    jogador2 =2

    while ganhou() == 0:
        print('\njogador', jogador1)
        exibe()
        linha = int(input('\nlinha :'))
        coluna = int(input('coluna'))
        if Board[linha -1][coluna -1] ==0:
            if (jogador1)==1:
                jogador2
                Board[linha-1][coluna-1]=1
            else:
                Board[linha-1][coluna-1]=-1
        else:
            print('já tem gente')
            jogada-=1
        if ganhou():
            print("Jogador ",jogada," ganhou apos ", jogada+1," rodadas")
         






Board =[ [0,0,0],
         [0,0,0],
         [0,0,0] ]
        
menu()
              





"""

