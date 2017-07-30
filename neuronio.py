

from decimal import *
from random import *

class NeuronioLogico:

    def __init__(self):
        self.limite_ciclos = 0
        self.portas = []
        self.pesos = {}
        self.pesos_iniciais = []
        self.taxa_aprendizado = 0

        self.inicializar()

    def inicializar(self):
        self.limite_ciclos = int(randrange(1, 11)*10.0)
        for i in range(3):
            p = Decimal(str(float(randrange(-10, 11)/10.0)))
            self.pesos_iniciais.append(p)

        self.taxa_aprendizado = Decimal(str(float(randrange(1, 11)/10.0)))

    def custo(self, erro):
        s = 0.0;
        for e in erro:
            s += e**2;
        s = s / 2;
        return s;

    def campoLocal(self, entradas, pesos):
        v = Decimal('0.0');
        #exemplo de entradas
        r = len(entradas)-1;
        for x in range(r):
            p = pesos[x]*Decimal(entradas[x])
            v = v + p;
        v = v + pesos[x+1]*1; #para o bias
        return v;

    def funcaoAtivacao(self, v):
        if v<0:
           y = 0;
        else:
           y = 1;
        return y;

    def treinar(self, porta):

        # definindo a taxa de aprendizado
        #n = Decimal(str(randrange(1, 10)/10.0));
        n = self.taxa_aprendizado #Decimal('0.9')
        pesos=[]
        e = porta.entradas[0]
        # se quizer fixar os pesos comente essas linhas (acrescente # no inicio delas)

        if self.pesos_iniciais is None:
            # definindo pesos iniciais aleatoriamente
            for i in range(len(e)):
                   p = Decimal(str(float(randrange(1, 10)/10.0)))
                   pesos.append(p)
        else:
            pesos = self.pesos_iniciais

        """
        if len(e)==3:
            pesos = [Decimal("0.7"), Decimal("0.1"), Decimal("0.6")]
        else:
            pesos = [Decimal("1.1"), Decimal("0.7"), Decimal("1.3"), Decimal("-2.9")]
                    #[Decimal("0.2"), Decimal("0.7"), Decimal("0.4"), Decimal("0.7")]
        """
        epocas = 0
        print 'Taxa de Aprendizado:', n
        print 'Pesos Iniciais:', pesos
        while 1:
            # lendo cada linha
            epocas += 1
            erros=[]
            for entrada in porta.entradas:
                #calculando o campo local induzido
                v = self.campoLocal(entrada, pesos)

                #calculando a funcao de v
                y = self.funcaoAtivacao(v)

                #calculando o erro
                pos_desejada = len(entrada)-1
                d = int(entrada[pos_desejada])
                erro = d - y
                erros.append(erro)
                #aplicando o ajuste
                qtde_pesos = len(entrada)
                #print pesos
                for x in range(qtde_pesos):
                        #delta = Decimal(str(round(n,2)*erro*int(entrada[x])))
                        #pesos[x]=Decimal(str(round(pesos[x],2)+round(delta,2)))
                        delta = Decimal(str(n*erro*int(entrada[x])))
                        pesos[x]=Decimal(str(pesos[x]+delta))
                # para o bias
                delta = n*erro*1
                #print delta
                #pesos[qtde_pesos-1] = Decimal(str(round(pesos[qtde_pesos-1],2)+round(delta,2)))
                pesos[qtde_pesos-1] = Decimal(str(pesos[qtde_pesos-1]+delta))

            c = self.custo(erros)


            if c==0:
                self.pesos[porta.nome] = pesos
                break

            # verificando o limite de epocas de treinamento
            if (self.limite_ciclos!=0 and epocas==self.limite_ciclos):
                print 'Atingie o limite de epocas de treinamento'
                break

        print 'Epocas de treinamento:', epocas
        print 'PESOS FINAIS:', pesos

    def testar_exemplo(self, porta, entradas):
        pesos = self.pesos[porta]
        c = self.campoLocal(entradas, pesos)
        return self.funcaoAtivacao(c)
