class PortaLogica:
    nome='';
    entradas=[];
    def __init__(self, nome, entradas):
        self.nome = nome
        self.entradas= entradas

    def linha(self, index):
        return self.entradas[index]

    def __str__(self):
        r = self.nome + '\n'
        for e in self.entradas:
            for i in e:
                r += i + ' '
            r += '\n'
        return r
