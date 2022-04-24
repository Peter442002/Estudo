#Pedra Papel Tesoura:
"""from random import random
player1 = ""
player2 = ""


def jogo():
    def pedra_papel_tesoura1 ():
        valor = random()
    #        print(valor)
        if  0.66 > valor > 0.33 :
            return f"{player1}a\n \tPedra"
        elif valor > 0.66:
            return f"{player1}\n \tPapel"
        return f"{player1}a\n \tTesoura"

    def pedra_papel_tesoura2 ():
        valor = random()
    #        print(valor)
        if  0.66 > valor > 0.33 :
            return f"{player2}a\n \tPedra"                                             
        elif valor > 0.66:
            return f"{player2}\n \tPapel"                                            
        return f"{player2}a\n \tTesoura"  """
#5Q's
"""
1- Quais os dados de entrada.
2- O que devo fazer?
3- Quais as restriçoes. 
4- Qual resultado esperado?
5- Qual a sequencia de passos a ser feito para alcançar o resultado?

Realizar o pseudocodigo...


"""
#Links 
"""
https://docs.python.org/3/library/collections.html







"""
#Funcoes antigas 1
"""
paises2 = dict(Br="Brasil", Eua= "Estados Unidos", Ca= "Canada")

C = None
V = None
paises3 = None

while True:
    print("Digite a Chave")
    x = input()
    if x in paises2:
        print(f"Encontrei!\n")
        print(x)
        print(paises2[x])
    else:
        print("\nAdicionar ao Dicionario\n digite a Chave")
        C = input()
        print("Digite o Valor\n")
        V = input()
        paises2[C] = V
        paises3 = paises2.copy()
        print("\nChave adicionada!\n")
        break     
print(paises3)

_________________________________________________________________________________________


Friend = {"Peter, Baiano, Toddy's, Rob"}
print(Friend)
Hortfruit

x = 0
s = {1, 2, 2, 3, 4, 5, 5, 2, 3, 5, 6}
d = {}.fromkeys({1: 2, 2: 3, 4: 5, 5: 2, 3: 5,}, f"{x + 1}")
t = (1, 2, 2, 3, 4, 5, 5, 2, 3, 5, 6)
l = [1, 2, 2, 3, 4, 5, 5, 2, 3, 5, 6]

print(s)
print(type(s))
print(len(s))
print(d)
print(type(d))
print(len(d))
print(t)
print(type(t))
print(len(t))
print(l)
print(type(l))
print(len(l))


#for x in range(1, 20):
#    print(x)
#    print(type(x))

__________________________________________________________________________________________

cidades = ["belo Horizonte", "Sao paulo", "Campo Grande", "Brasilia", "Rio de Janeiro", "Cuiaba", "Sao paulo", "Sao paulo", "Campo Grande", "Brasilia", "Rio de Janeiro", "Cuiaba", "Sao paulo"]
cidade = set(cidades)

print(cidades)
print(cidade)

print(len(cidades))
print(len(cidade))


__________________________________________________________________________________________

           #Entrada dados da Rede



ativo = True
logado = True


if ativo or logado:
    print("Seja bem vindo(a), Escreva Seu nome")
    elif ativo == False:
        print('Você esta desconectado!, precione "ctrl" + "Shift" + "R"')
        elif logado == False:
            print("Você ja esta logado, deseja deslogar?"'digite "1" para sim, ou "0" para nao')
            bool.input()

            #Entrada do nome
nome = input().title()

            #Saida do nome
print(f'Seja Bem-vindo(a) {nome}')

            #Entrada da Idade
print("Qual sua idade")
idade = int(input())
            #saida da idade
if idade < 18:
    print(f"Menor de idade, {idade}")
elif idade >100:
    print(f"idade falsa {idade}, Voce teria de ter nascido em {2022 - int(idade)}")
    print(f"Você {nome} realmente tinha que fazer gracinha!? continua essa bosta...")
    
            #Entrada de Sexo
print("Qual o seu sexo?")
sexo = input().title()

            #Saida de Sexo
print(f"Você se define pelo sexo {sexo}")

x = int(input("How many times do you want do this? "))
for y in range(1, x+1):
    print(f"Imprimindo {y}")

__________________________________________________________________________


x = 10

print("\n Seja Bem-vindo!")
while True:
    cpf = input("\n Digite Seu CPF\n")

    if cpf == "782.809.586-49":
        print("\n CPF cadastrado\n Logando...\n")
        break
    
    elif cpf != ("782.809.586-49"):
        x = (x - 1)
        print(f"\n Tente novamente, você tem mais {x}, tentativas.")
        if x == 0:
            print("\n Conta Bloqueada! \n Espere (10)min")
            break

_________________________________________________________________________

"""
#Estruturas
"""

        Udemy
login = thalles1809@gmail.com
Thalles@200106

Dir -> aprensenta todos os atributos e funçoes/metodos disponiveis para determinado tipo de dado ou variavel.
dir(x)


Help -> aprensenta a documentaçao/como utilizar os atributos/prpriedades e funçoes/metodos disponiveis para determinado tipo de dado ou variavel.

help(x.y)


                                    * Condicionais

        If (se)
            Else (se nao, final)
                elif (se nao, de continuaçao)

                                    * Estruturas Logicas
    Operadores Binarios: 

            {And (e), or (ou), is (é)}
       #Para "and", ambos tem que ser True.
            #Para "or", um ou outro valor precisa ser True.
                #Para "is", o valor é comparado com outro

    Operadores Unarios:
            {not (nao)}
        #Para "not" o valor do booleano é invertido, (se for True vira false), (se for False vira True);
      
                                    * Repetiçao

    Loop:
        For: itera os valores em sequencia

            #for letra in nome:
                print(letra)

                                    * 
    


"""
#Listas
"""
Listas em python funcionam como vetores/ matrizes, com diferença de serem DINAMICO e tambem
 de podermos colocar QUALQUER tipo de dado.

- DINAMICO:
    -Nao possui tamanho fixo;
    ou seja criamos a lista e simplesmente ir adicionando elementos;
        - Qualquer tipo de dado: Nao possuem tipo de dado fixo;
        As listas de python sao representadas por Colchetes: [];

    
                                        Para ordenar uma lista:
                *list.sort() -> {Do menor para o maior}   *list.reverse / [::-1]  -> {Reverte a ordem}

                                        Para contar repeticoes de um elemento:
                *list.count()

                                        Para adicionar elementos em listas:
                *append(x) < extend(x)                                                obs:appedn só pode 1 elemento.

                                        Para adicionar elemento informando a posiçao do índice:
                *insert(indice, valor)

                                        Para juntar duas listas:
                *list(x) = list(x) + list(y)

                                        Para Copiar uma lista:
                *list(x) = List(y).copy()

                                        Para saber o tamanho de uma lista:
                *print(len(listx))

                                        Para remover facilmente o ultimo elemento de uma lista ou o elemento do indice indicado:
                *listx.pop(x)                                                        obs: Tanto remove o ultimo como retorna.

                                        Para remover todos os elementos:
                *listx.clear()

                                        Para repetir uma lista:
                *listx = lixtx * 3
                
                                        Para converter uma string em uma lista:
                *x = x.split()                                               obs: por padrao ele separa os elementos da lista, que estao separados pelo espaço.

                                        Para converter de lista para string:
                *x = "y".join(list)

                                        Para encontrar o indice de um elemento na lista:
                *print(lista.index(x,(Indice do inicio da busca), (indice do final da busca))                 obs: Retorno o indice do primeiro valor encontradores

                                        Para pegar os elementos de uma lista ou range:
                *print(lista[inicio:Fim:Intervalo])

                                        Para saber a soma de uma lista:
                *print(sum(lista))

                                        Para imprimir o maior valor de uma lista:
                *print(max(lista))

                                        Para imprimir o menor valor de uma lista:
                *print(min(lista))

                                        Para Transformar em uma lista em tuplas:
                *list = tuple

                                        Para desempacotar uma lista:
                *lista = [1, 2, 3] 
                num1, num2, num3  => num1 = 1...                        obs: o numero de elemtos e variaveis devem ser iguais.

"""
#Tuplas
"""

                                                    
                                                                    #Tuplas

                                                            tuple(inicio:Fim:Passo)


                Tuplas sao bastante parecidas com listas, existem basicamente duas diferenças basicas:

                1- as tuplas sao representadas por ()

                2- As tuplas sao imutaveis:
                    isso significa que ela nao muda, toda operaçao em uma tupla gera uma nova tupla.

                (4) -> Não é tuplas 
                (4,) -> É tupla
                4, -> É tupla

                Tuplas sao mais rapidas que as listas para serem lidas.
                tuplas deixam o codigo mais seguro.

                        Devemos utilizar tuplas sempre que nao precisamos mudar os dados contidos dentro da tupla:
                Valores Fixos, imutaveis...
                Ex: Meses, anos....

"""
#Dicionarios/Mapas
"""
                                            Mapas

            Em Python mapas sao conhecidos como Dicionarios
        Dicionarios sao representados por {}

                                            Dicionarios


            obs: em algumas liguagens dicionarios sao conhecidos como mapas
        Dicionarios sao coleçoes do tipo chave/valores

        Dicionarios sao representados por {}
            - Chave/Valor podem ser de quaisquer tipo de dados;
            - Podemos misturar dados;

print(type({}))

dicionario = {chave: valor,}
        Criaçao de dicionarios:

                #Forma 1
        
paises = {"Br": "Brasil", "Eua": "Estados Unidos", "CA": "Canada"}

                #Forma 2

paises2 = dict(Br="Brasil", Eua= "Estados Unidos", Ca= "Canada")


                                                        Para acessar elementos:
                #Forma 1
            print(paises["Br"])


                #Forma 2
            print(paises.get("Br"))                                                     obs: o get caso falso retorna None, o que faz nao gerar erro KeyError.

                                                        Para adicionar elementos:

                #Forma 1
            Dict["chave"] = Valor

                #Forma 2
            Dict.update({"chave": Valor})


                                                        Para Remover Dados de um Dicionario:
                #Fora 1
            Dict.pop("chave")

                #Forma 2
            del Dict["Chave"]                                         
                            
                                                        Para limpar o dicionario:
            
            Dict.clear()

                                                        Para copiar um dicionario para outro:
            
                    #Forma 1
            Dict1  = dict.copy()  #Deep copy

            Dict1 = Dict          #Shallow copy
                            

                                                        Fronkeys:
            Dict = {}.fromkeys( Chave, Valor )

                                                        Dicionario de Chaves:
            print(dict.keys())

                                                        Exibir valores:
            print(dict.values())

                                                        Descompactando Dicionario, em tuplas:
            print(Dict.items())

                                                        Para saber o Valor maximo, soma, minimo e tamanho:
            print(sum(Dict.values()))
            print(max(Dict.values()))                                                                              
            print(min(Dict.values()))  
            print(len(Dict.values()))





"""
#None
"""
                None em Python

        o tipo None em python sempre sera False.

        O tipo de dado None em python representa o tipo sem tipo, ou poderia ser conhecido tambem
        como o tipo vazio, porém, falar quem é um tipo sem tipo é mais apropriado.


        Quanto utilizamos?

            - Podemos utilizar None quando queremos criar uma variavel e inicializa-la com um tipo sem tipo antes de recebermos um valor final.

numeros = None
....

numeros = (1, 5, 6...)

"""
#Conjuntos
"""
                            Conjuntos
    
         - Quando falamos de conjuntos em quaisquer liguagem de programaçao, estamos fazendo teoria de teoria
        dos conjuntos da Matematica.

         - Podemos ter varios tipos de dados nos Sets
         - Mutavel

         - Aqui no python, os conjuntos sao chamados de Sets.

         - Dito isso, da mesma forma que na matematica:

          *Sets (conjuntos) nao possuem valores duplicados;
          *Sets (conjuntos) nao possuem valores ordenados;
          *Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados;

        Conjunto sao bons para se utilizar quando precisamos armazenar elementos mas nao nos importamos com a ordenaçao deles.
        Quando nao precisamos se preocupar com chaves. valores e itens duplicados.

        - Os conjuntos (Sets) sao referenciados em Python com chaves {}

        Diferença entre Conjuntos (Set) e mapas (Dicionarios) em Python:
            - Um dicionario tem Chave/Valor;
            - um Conjunto tem apenas Valor;

                Onde usar um set

            - Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes,
            informaram manualmente a cidade de onde vieram.


cidades = ["belo Horizonte", "Sao paulo", "Campo Grande", "Brasilia", "Rio de Janeiro", "Cuiaba", "Sao paulo", "Sao paulo", "Campo Grande", "Brasilia",]

print(len(set(cidades)))
         


                                    *Para adicionar elementos no conjuntos:
        set.add(x)

                                    *Para Remover um item:
        #Forma 1: 
            set.remove(x)                                           obs: x = o valor a ser removido, sets nao sao indexados
                
        #Forma 2:
            set.discard(x)                                                                        

                                    *Para descobrir a uniao:
        
        #Forma 1
            x.union(y)

        #Forma 2
            x = x|y 
        
                                    *Para descobrir a interceçao:

        #Forma 1
            x = x.intersection(y)

        #Forma 2
            x = x & y                            

                                    * Para descobrir a diferença

        a = x.difference(y)
        b = y.difference(x)


"""
#Collections - counter (high performance)
"""
                            Collections - counter
    
    collections -> high-performance Container Datetypes


    Counter -> recebe um interavel como parametro e cria um objeto do tipo collections counter que é parecido
com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.

    -Podemos usar o Couter com qualquer valor.

    para utilizar é necessario importar o Counter:

from collections import Counter

lista = (10,10,1,2,2,2,2,2,2,2,2,2,2,2,1,2,11,12,13,6/3)  
res = Counter(lista)
print(res)

=> Counter({2: 13, 10: 2, 1: 2, 11: 1, 12: 1, 13: 1})

            #Como resultado ele retorna cada palavra ou inteiro como uma chave e como valor o numero de vezes que aparece.


                                    Para saber as chaves que mais retornaram:
        print(res.most_common(x))       x = numero  de chaves a serem retornadas. 

"""
#Default - Dict (high performance)
"""     
                Modulo Collections - Default Dict

    Todas as funcoes validas para o Dict valem para o Default Dict

        Default Dict -> Ao criar um dicionario utilizando-o, nós informamos  um valor default,
    podendo utilizar um lambda para isso. Este valor sera utilizado sempre que nao houver um valor definido.
    Caso tentemos acessar uma chave que nao existe, esa chave será criada e o valor default será atribuido.


            Obs: Lambdas sao funcoes sem nomes que podem ou nao receber parametros de entrada e retornar valores.

                É necessario importar o Default Dict 

from collections import defaultdict

            Quando solicitado uma chave nao presente no dicionario ele nao retorna "KeyError", mas sim cria uma nova
        chave com o valor ja pré-programado.

######################################## Uso #######################################################################
from collections import defaultdict
x = None
dict = defaultdict(lambda: x)

dict["Arroba"] = "saitama"

print(dict)

print(dict["Arroba"])
print(dict["Outro"])


"""        
#Ordered - Dict (high performance)
"""

                Modulo Collection: Ordered Dict

        *OrderedDict -> É um dicionario, que nos garante a ordem de inserçao dos elementos.
        

            É necessario fazer o Import

from collections import OrderedDict

dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}

################################ uso #################################
from collections import OrderedDict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}

print(dict1 == dict2) #True -> ja que a ordem nao importa.



odict1 = OrderedDict({"a": 1, "b": 2})
odict2 = OrderedDict({"b": 2, "b": 1})

print(odict1 == odict2) #False -> ja que a ordem importa.
"""
#Named Tuple (high performance)
"""
                Modulo Collections - Named Tuple
    *Sao Tuplas, Diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.

    #precisamos definir um nome e parametros

        Import
from collections import namedtuple



        #Forma 1
        
chachorro = namedtuple("cachorro", "idade raca nome")

        #Forma 2

chachorro = namedtuple("cachorro", "idade, raca, nome")

        #Forma 3

chachorro = namedtuple("cachorro", ["idade, raca, nome"])



########################## Uso #####################################
from collections import namedtuple

cachorro = namedtuple("cachorro", ["idade", "raca", "nome"])

negao = cachorro(idade=5, raca="Pastor Belga", nome= "Negao")

print(negao)

#Forma 1

print(negao[0])     #idade
print(negao[1])     #raça
print(negao[2])     #nome

#Forma 2

print(negao.idade) 
print(negao.raca)
print(negao.nome)


"""
#Deque (high performance)
"""
                    Modulo Collections - Deque

            É semelhante a uma lista.

    Import
from collections import deque

###################### uso ##################################################
from collections import deque

deq = deque ("Fodase")
print(deq) 

#Adicionando elementos.

deq.append(" 1") #Adiciona no ultimo elemento
deq.appendleft("2 ") #Adiciona no primeiro elemento

print(deq)

lista = ("geek")
print(lista)

#Removendo elementos.

print(deq.pop()) #Remove o ultimo elemento
print(deq)

print(deq.popleft()) #Remove o primeiro elemento
print(deq)

"""
#Definindo funçoes
"""
                Definindo funçoes: 
    

    - Funçoes sao pequienos trechos de código que realizam tarefas específicas;
    - Pode ou nao receber entradas de dados e retornar uma saida de dados;
    - Muito iteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma funçao que realiza varias tarefas dentro dela;
é bom fazer uma verifcaçao para que a funçao seja simplificada.

funcoes basicas:
- print ()
- len ()
- max ()
- mim ()
- count ()
...

            # Em python a forma gerao de definir uma funçao é:
    def nome_da_funcao(parametros_de_entrada):
        bloco_da_funcao

onde:

nome_da_funçao ->           SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case):
Parametros_de_entrada ->    Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou nao>
bloco_da_funcao ->          Tambem chamado de corpo da funcçao ou implementaçao, é onde o processamento da funçao acontece.

OBS: Veja que para definir uma funçao, utilizamos a palabra reserbada "def" informando ao Python que estamos definindo uma funçao.
Tambem abrimos o bloco de codigo com o ja conhecido dois pontos : que é utilizado em Python para definir blocos.

Teste:

                #Definindo a funçao
            def diz_oi():
                print("oi!")

OBS:
1- Veja que dentro das nossa funcçoes podemos utilizar outras funçoes;
2- Veja que nossa funçao só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3- Veja que esta funçao nao recebe nenhum parametro;
4- Veja que esta funçao nao retorna nada;


                #Chamando a funcao
            diz_oi()

OBS: Nunca se esqueça de abrir e fechar o parenteses ao executar uma funçao.

#Em Python, podemos inclusive criar uma variaveis do tipo de uma funçao e executar esta funçao atravez da variavel.

            diz = diz_oi
            diz()


"""
#Funçoes Com Retorno
"""
OBS: Em Python, Quando uma funçao nao retorna nenhum valor, o retorno é None

OBS: Funçoes em pyhton que retornam, devem retornar estes valores com a palavra reservada "Return"

OBS: Nao precisamos necessariamente criar uma variavel para receber o retorno de uma funçao.
Podemos passar a execuçao da funçao para outras funçoes.


OBS: Sobre a palavra reservada return
1- Ela finaliza a função, ou seja, ela sai da execuçao da funçao;
2- Podemos ter, em uma função, diferentes returns;
3- Podemos, em uma funçao, retornar qualquer tipo de dado e até mesmo multiplos valores;

exemplos OBS:
1- 
def diz_oi():
    print("estou sendo executado antes do return...")
    return "oi!"
    print("estou sendo executado depois do return...")   (essa funçao nao é realizada)

2-
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "b"

3- 
def nova_funcao():
    return 1/20, "amor", True, 5.5

num1, num2, num3, num4 = nova_funcao()
print(num1, num2, num3, num4)


################## Uso ################################################################

def quadrado_de_7():
    return 7*7

"""
#Funçoes com parametro (de entrada)
"""
- Funçoes que recebem dados para serem processados dentro da mesma;

se a gente pensar em um programa qualquer, geralment temos:

entrada -> processamento -> saida

Se a gente pensar em uma funçao, ja sabemos que temos funçoes que:
- Nao possuem entrada;
- Nao possuem saída;
- Possuem entrada mas nao possuem saída;
- Nao possuem entrada mas possuem saída;
- Possuem entrada e saída;

############## Uso #####################################################
def quadrado_de_7(numero):   *dentro do parenteses é o parametro.
    #return numero * numero
    return numero ** 3
    
print(quadrado_de_7(7)) 
print(quadrado_de_7(2)) 
print(quadrado_de_7(5))


    #funçoes podem ter x parametros de entrada. Ou seja, podemos receber entrada para
em uma funçao quantops parametros forem necessarios. Eles sao separados por virgulas.

def soma(a, b, c):
    return a + b * c

def miltiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

    # Nomeando parâmetros

def nome_completo(nome, sobrenome)
    return f"Seu nome completo é {nome} {sobrenome}
print (nome_completo("Paul", "Brian"))

    # A diferença entre parâ metros e Argumentos
Parametros sao variaveis declaradas na definiçao de uma funçao;
Argumentos sao dados passados durante a execuçao de uma funçao;

OBS: A ordem dos parametros importam

    #Forma em que a ordem nao importaria:
print(nome_completo(nome="angelina", Sobrenome="jolie"))
Resultado: angelina jolie
print(nome_completo(sobrenome="marquesine", nome="Bruna"))
resultado: Bruna marquesine

    
"""
#Funçoes com parametro padrao
"""
         Funçoes onde a passagem de parametro seja opcional

- Nos permite ser mais flexiveis nas funçoes;
- Evita erros com parametros incorretos;
- Nos permite Trabalhar com exemplos mais legiveis de codigo;
- Podemos usar qualquer tipo de dado como Defaults


print("Foda-se")

=> Correto

print()

=> Correto


def exponencial (numero, potencia=2): #o "=2" gera o valor padrao caso nao seja informado a potencia
    return numero ** potencia
 
print(exponencial())

OBS: Em funçoes Python, os parametros com valores default (padrao) DEVEM sempre estar ao final da declaração.

#ERRO
def teste(num=2, potencia):
    return num ** potencia

Ex: avançado
def mostrar_informacao(nome='geek', instrutor=False):
    if nome =='geek' and instrutor:
        return"Bem-vindo Instrutor geek"
    elif nome == "geek":
        return "eu pensei que vc era o instrutor, entao foda-se"
    return f"olá {nome}"

print(mostrar_informacao())
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao(True))
print(mostrar_informacao("Peter"))
print(mostrar_informacao(nome="Peter"))
"""
#Trazendo alteraçoes da Variavel Local para a Global
"""
total = 0

def incrementa():
    global total #Avisando que queremos utilizar a avariavel global
    total = total + 1
    return total
print(incrementa()) #1
print(incrementa()) #2
print(incrementa()) #3
"""
#Usar no pedra papel 
# aradas dentro de funçoes, e tambem tem uma forma especial de escopo de variavel
"""
            - nonlocal > utiliza a variavel da funçao anterior
 
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador =contador + 1
        return contador
    return dentro()
"""
#Docstrings
"""
            - Documentando funçoes em Docstrings
- Escrever o motivo da função
- Coisas importantes para

OBS: Podemos ter acesso a documentaçao de uma funçao em Python
utilizando a propriedade especial __doc__.
ou utilizando a funçao help

Ex:
def diz_oi():
    "Uma funçao simples que retorna a string 'oi'"
    return "Oi! "

help(diz_oi)
print(diz_oi.__doc__)

Ex 2:
def exponencial(numero, potencia=2):
    ""
    Funçao que retorna por padrão o quadrado de um 'numero' ou 'numero á 'potencia' informada.
    :Parametro numero: Número que desejamos gerar o exponencial.
    :Paramametro potencia: Pòtencia que queremos gerar o exponencial. Por padrão é 2.
    :return: retorna o exponencial de 'numero' por 'potencia'.
    ""
    return numero ** potencia


"""
#*Args
"""
                    Entendendo o *Args

-Abstrai informaçao do tipo Tupla?

- O *args é um parametro, como outro qualquer, isso significa que voce poderá chamar
 de qualquer coisa, desde que começe com asterisco.

Ex:
*xis

Mas por conveçao, utilizamos *args para definí-lo

- O * Informa para o python que estamos passando uma coleçao de dados, logo o python necessitara desempacotar os dados;
ex:
def soma(*args):
    return sum(args)

numeros = [1,2,3,4,5,6]

print(soma(*numeros))


Mas o que é o *args?

O parâmetro *args uitilizado em uma funçao, coloca os valores extras informados
como entrada em uma tupla. Entao desde ja lembre-se que tuplas sao imutaveis.

def soma_todos_numeros(*args):
    ""Esta funçao soma todos os argumentos inceridos""
    return sum(args)


def verifica_info (*args):
    if "Amor" in args and "seu" in args:
        return "Bem-vindo amor"
    return "eu nao tenho certeza quem voce é..."


print(verifica_info())
print(verifica_info(1, True,"seu", "Amor"))
print(verifica_info(1, "seu", 3.145))
"""
#**Kwargs
"""
                    **Kwargs

- abstrai informaçao para como dicionario com chave e valor...

Este é só mais um parametro, Mas diferete do *args que coloca os valores extras em uma tupla, o **kwargs exige que eutilizemos parametros
nomeados, e tranforma esses parametros extras em um dicionario.

Ex:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items ():
        print(f"A cor Favorita de {pessoa.title()} é {cor}")

cores_favoritas(Marcos = "verde", Julia="amarelo", Fernanda= "Azul", Vanessa="Branco")

Ex2:
def cumprimento_especial (**kwargs):
    if "geek" in kwargs and kwargs ["geek"] == "python":
        return "Você recebeu um cumprimento Pythonico geek"
    elif "geek" in kwargs:
        return f"{kwargs['geek']} geek!"
    return "nao tenho certeza quem você é..."

print(cumprimento_especial())
print(cumprimento_especial(geek="python"))
print(cumprimento_especial(geek="oi"))
print(cumprimento_especial(geek="especial"))

                            *Nas nossa funçoes, podemos ter: (Nesta Ordem)

        -Parametros Obrigatorios;
        -*args
        -parametros default (nao Obrigatorios);
        - **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    return(kwargs)

minha_funcao(8, "julia")
minha_funcao(18, "Felicity",4,5,3, solteiro=True)
minha_funcao(34, "felipe", eu="nao",voce="vai" )
minha_funcao(19, "Carla", 9,4,3, java=False, python=True)

"""
#desempacotar **kwargs
"""
Ex:
def mostra_nomes(**kwargs)
    return f"kwargs{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'felicity', 'sobrenome': 'jones'}

print(mostra_nomes(**nomes))

=> Felicity Jones



def soma_multiplos_numeros(a,b,c):
    print(a + b + c)

lista = [1,2,3]
tupla = 1,2,3
Set = {1,2,3}

soma_multiplos_numeros(*lista )
soma_multiplos_numeros(*tupla )
soma_multiplos_numeros(*Set )

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario )
"""
#list comprehensions
"""

                List comprehension 
    
    
    - utilizando list comprehension nos podemos gerar novas listas com dados processados a partir de outro iteravel.
    -Nós podemos adicionar estruturas condicionais lógicas as nossas list comprehensions

#Sintaxe da List comprehension

                                            *[ dado for dado in iteravel]

Ex1:
numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]
 
print(res)

        * Para entender melhor o que esta acontecendo devemos divir em duas partes:
    -A primeira parte: for numero in numero
    -A segunda parte: numero * 10

Ex2:
numeros = [1,2,3,4,5]


def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

            Modo Mediano:
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

            Modo Avançado:
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

ex:

numeros = int([1,2,3,4,5,6])

pares = [numero for numero in numeros % 2 == 0]
impares = [numero for numero in numeros % 2 != 0]

print(pares)
print(impares)
"""
#Lista Aninhadas - Matrizes
"""
                    Listas aninhadas
    

numeros = [1, "b", 6.22, True, 5]

ex sem comrpehension:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas[0])
=> [1, 2, 3]

print(listas[0][1])
=> [2]

iterando com loops em uma lista aninhada:

            ex comprehension:
            listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            [[print(valor) for valor in Lista] for Lista in listas]



tabuleiro = [[numero for numero in range(1, 10)] for grupos in range(1, 4)]
print(tabuleiro)
"""

