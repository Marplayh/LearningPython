import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentarNovamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentarNovamente == True:
            if int(self.Valor_do_chute) > self.valor_aleatorio:
               print('Chute um valor mais baixo!')
               self.PedirValorAleatorio()
            elif int(self.Valor_do_chute) < self.valor_aleatorio:
               print('Chute um valor mais alto!')
               self.PedirValorAleatorio()
            if int(self.Valor_do_chute) == self.valor_aleatorio:
                self.tentarNovamente = False
            print('Parabens você acertou!')

    def PedirValorAleatorio(self):
        self.Valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
