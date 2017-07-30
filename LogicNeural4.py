#! /usr/bin/python

from decimal import *

from porta import PortaLogica
from neuronio import NeuronioLogico

portas=[]

neuronio = NeuronioLogico()

opcoes_menu={}

qtde_entradas =  0

def imprimir(porta):
    print porta.nome,
    for e in porta.entradas:
        for i in e:
            print i,
        print ''

def ler_arquivo():
    global portas
    portas = []
    fil = open("input.txt")
    a = fil.readlines()
    i = 0
    tam = len(a)
    while 1:
        nome = a[i]
        nome = nome[0:nome.find('\n')]
        i = i + 1
        entradas = []
        item = a[i]
        item = item[0:item.find('\n')]
        while (item!=''):
            entradas.append(item.split())
            i = i + 1
            item = a[i]
            item = item[0:item.find('\n')]

        p = PortaLogica(nome, entradas)

        portas.append(p)
        i = i + 1
        if (i==tam):break
    fil.close()

def mostrar_portas():
    print 'Porta logica'
    for p in portas:
        print p

def salvar():
    print 'ainda nao implementado'
    """
    fil = open("output.txt")
    for p in neuronio.pesos.keys():
        print p, neuronio.pesos[p]
    """

def treinar():
    porta = raw_input('Informe a porta que deseja treinar () : ')
    for p in portas:
        if porta==p.nome:
            print 'Treinando a porta:'
            neuronio.treinar(p)
        print '==================='

    print neuronio.pesos

def definir_pesos():
    neuronio.pesos_iniciais=[]
    q = raw_input('Informe os pesos separados com espaco e ponto para separar casas decimais:')
    for p in q.split():
        neuronio.pesos_iniciais.append(Decimal(p))

def testar_exemplo():
    p = raw_input('Informe a porta que deseja testar: ')
    e = raw_input('Informe as entrada separadas por espaccos: ')
    e = e.split()
    r = neuronio.testar_exemplo(p, e)
    s = e[0]
    for i in e[1:len(e)]:
        s += ' AND ' + e[1]
    s += ' = ' + str(r)
    print s

def definir_limite():
    limite = raw_input('Informe o limite de epocas de treinamento: ')
    neuronio.limite_ciclos = int(limite)

def sair():
    print 'tchau...'

def definir_taxa_aprendizado():
    neuronio.taxa_aprendizado = Decimal(raw_input('Informe a taxa de aprendizado: '))

def mostrar_portas_aprendidas():
    print neuronio.pesos

opcoes_menu = {
        1: ler_arquivo,
        2: mostrar_portas,
        3: definir_pesos,
        4: definir_limite,
        5: definir_taxa_aprendizado,
        6: treinar,
        7: salvar,
        8: testar_exemplo,
        9: mostrar_portas_aprendidas,
        0: sair
    }

def menu():
    print '1 - Ler arquivos com exemplos'
    print '2 - Mostrar portas lidas'
    print '3 - Definir pesos iniciais ', neuronio.pesos_iniciais
    print '4 - Definir limite de epocas de treinamento', neuronio.limite_ciclos
    print '5 - Definir taxa de aprendizado ', neuronio.taxa_aprendizado
    print '6 - Treinar '
    print '7 - Salvar '
    print '8 - Calcular exemplo '
    print '9 - Mostrar portas aprendidas'
    print '0 - Sair'

    opcao = raw_input('Digite sua escolha:')
    print 'Sua escolha foi', opcao
    return int(opcao)


def main():
    while 1:
        opcao = menu()
        opcoes_menu[opcao]()

        if opcao==0:
            break





if __name__ == "__main__":
    main()
